import re, os, json, glob

ROOT = "/Users/etech/Desktop/MLT_&_DL/DL_Python/lectures"
OUT_DIR = "/Users/etech/Desktop/MLT_&_DL/DL_Python/site"
os.makedirs(OUT_DIR, exist_ok=True)

import markdown2

MD_EXTRAS = ["tables", "fenced-code-blocks", "code-friendly"]

LIST_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+\.\s+)")

def ensure_blank_before_lists(text):
    lines = text.split("\n")
    out = []
    for i, line in enumerate(lines):
        if LIST_RE.match(line):
            prev = out[-1] if out else ""
            if prev.strip() != "" and not LIST_RE.match(prev):
                out.append("")
        out.append(line)
    return "\n".join(out)

def md_to_html(text):
    text = ensure_blank_before_lists(text)
    return markdown2.markdown(text, extras=MD_EXTRAS)

lecture_dirs = sorted(
    glob.glob(os.path.join(ROOT, "Lecture *")),
    key=lambda p: int(re.search(r"Lecture (\d+)", p).group(1))
)

lectures = []
topic_index = {}  # id -> {"lecture": n, "title": ...}

for ld in lecture_dirs:
    num = int(re.search(r"Lecture (\d+)", ld).group(1))
    readme_path = os.path.join(ld, "README.md")
    readme_raw = open(readme_path, encoding="utf-8").read() if os.path.exists(readme_path) else ""

    # lecture title from first line of README: "# Lecture N [and M] — Title (course)"
    title = f"Lecture {num}"
    label = f"Lecture {num}"
    subtitle = ""
    hm = re.search(r"^#\s*(Lecture\s+[\d\s&,]*?(?:and\s*\d+)?)\s*—", readme_raw, re.MULTILINE)
    if hm:
        label = hm.group(1).strip()
    m = re.search(r"^#\s*Lecture\s*[\d\s]+(?:and\s*\d+\s*)?—\s*(.+)$", readme_raw, re.MULTILINE)
    if m:
        full = m.group(1).strip()
        # split off a trailing "(<course code>: ...)" parenthetical as subtitle
        pm = re.match(r"^(.*?)\s*\(([^()]*)\)\s*$", full)
        if pm:
            title = pm.group(1).strip()
            subtitle = pm.group(2).strip()
        else:
            title = full

    # source pdf line
    pdf_m = re.search(r"Source PDF:\s*`([^`]+)`", readme_raw)
    source_pdf = pdf_m.group(1) if pdf_m else ""

    readme_html = md_to_html(readme_raw)

    files = sorted(
        f for f in os.listdir(ld)
        if f.endswith(".md") and f != "README.md"
    )

    topics = []
    for fname in files:
        fid = fname[:-3]  # strip .md
        raw = open(os.path.join(ld, fname), encoding="utf-8").read()

        # topic title: first line "# Topic N: Title"
        tm = re.search(r"^#\s*(?:Topic\s*\d+:\s*)?(.+)$", raw, re.MULTILINE)
        topic_title = tm.group(1).strip() if tm else fid

        # source line "Source: ..."
        sm = re.search(r"^Source:\s*(.+)$", raw, re.MULTILINE)
        source_line = sm.group(1).strip() if sm else ""

        # split into sections on "## N) ..." headers
        parts = re.split(r"^##\s*\d\)\s*(.+)$", raw, flags=re.MULTILINE)
        # parts[0] = preamble (title+source+---), then alternating heading, body...
        sections = []
        for i in range(1, len(parts), 2):
            heading = parts[i].strip()
            body = parts[i + 1] if i + 1 < len(parts) else ""
            body = re.sub(r"^-{3,}\s*$", "", body, flags=re.MULTILINE)  # strip stray --- lines
            sections.append({"heading": heading, "html": md_to_html(body.strip())})

        topics.append({
            "id": fid,
            "title": topic_title,
            "source": source_line,
            "sections": sections,
        })
        topic_index[fid] = {"lecture": num, "title": topic_title}

    lectures.append({
        "num": num,
        "label": label,
        "title": title,
        "subtitle": subtitle,
        "source_pdf": source_pdf,
        "readme_html": readme_html,
        "topics": topics,
    })

# ---- cross-reference resolution: [[id]] or [[id]] from Lecture N ----
xref_pattern = re.compile(r"\[\[([A-Za-z0-9_]+)\]\](?:\s+from\s+Lecture\s+(\d+))?")

def resolve_xrefs(html, current_lecture):
    def repl(m):
        ref_id = m.group(1)
        ref_lec = int(m.group(2)) if m.group(2) else current_lecture
        info = topic_index.get(ref_id)
        if info:
            label = info["title"]
            lec = info["lecture"]
            return (f'<button class="xref" data-lec="{lec}" data-id="{ref_id}">'
                    f'<span class="xref-badge">L{lec}</span> {label}</button>')
        else:
            return f'<span class="xref-missing">{ref_id}</span>'
    return xref_pattern.sub(repl, html)

for lec in lectures:
    for topic in lec["topics"]:
        for sec in topic["sections"]:
            sec["html"] = resolve_xrefs(sec["html"], lec["num"])
    lec["readme_html"] = resolve_xrefs(lec["readme_html"], lec["num"])

# stats
total_topics = sum(len(l["topics"]) for l in lectures)
print(f"Lectures: {len(lectures)}, Topics: {total_topics}")

with open(os.path.join(OUT_DIR, "content.js"), "w", encoding="utf-8") as f:
    f.write("window.LECTURES = ")
    json.dump(lectures, f, ensure_ascii=False)
    f.write(";\n")

print("Wrote", os.path.join(OUT_DIR, "content.js"))
