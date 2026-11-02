"""
Generates site/labs_content.js from the Lab_assingments/ folder.

This is the "Lab Assignments" counterpart of build_site.py (which handles
lectures/). It is intentionally a separate script/output file so the
existing lecture pipeline (content.js) is never touched by this one.

For each "Lab Assignment N" folder, it:
  1. Reads the assignment's top module docstring as an "About this
     assignment" intro.
  2. Splits the .py file into zones using the big
         # ================...================
         # <TITLE, possibly multi-line>
         # ================...================
     banners already used consistently in every lab_assignment_N.py file.
  3. Groups zones into: "setup" (everything before the first QUESTION
     banner, plus any non-question banner that leads the file), one group
     per QUESTION number (sub-parts like "QUESTION 2A"/"QUESTION 2B" merge
     into "Question 2"), and "wrapup" (any non-question banner trailing
     after the last QUESTION banner, e.g. "SAVING ...").
  4. For each group, finds every section("...") call inside it (in code
     order) - these exact strings are also what gets printed as banner
     headings at runtime, so they double as delimiters we can use to slice
     the matching chunk of text out of that assignment's captured
     run_output.txt.
  5. Within each group's code, splits consecutive "#" comment lines
     ("explanation") apart from consecutive real code lines ("code"), so
     the site can render them as alternating teaching cards.
  6. Finds any plot PNGs (in a "plots" subfolder) whose filename starts
     with that question's number, and embeds them as base64 data URIs
     (so the whole site stays a handful of static files - no extra image
     folder to keep in sync when deploying).

Run with:
    <venv>/bin/python3 build_labs.py
"""
import re
import os
import sys
import json
import base64
import glob

ROOT = "/Users/etech/Desktop/MLT_&_DL/MLT_Python/Lab_assingments"
OUT_DIR = "/Users/etech/Desktop/MLT_&_DL/MLT_Python/site"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lab_explanations_i18n import TRANSLATIONS  # noqa: E402


def attach_explanation_styles(chunks, assignment_num, section_id):
    """For every "explanation" chunk, attaches all 3 reading styles:
      - "simple"    : the auto-extracted comment text itself (unchanged -
                      this IS the plain-English style, at zero extra cost,
                      since every lab script's comments were already
                      written for a total beginner).
      - "technical" : a hand-written, more precise/formal rewrite, from
                      lab_explanations_i18n.py.
      - "hinglish"  : a hand-written Hinglish (Roman Hindi+English) version
                      of the same explanation, from the same file.
    Falls back to the "simple" text for any style not yet authored there,
    so a not-yet-translated assignment still renders correctly (all 3 tabs
    just show identical content until it's written) instead of breaking.
    Code chunks pass through untouched - only one, real, unstyled version
    of the actual runnable code ever exists."""
    section_translations = TRANSLATIONS.get(assignment_num, {}).get(section_id, [])
    result = []
    for chunk in chunks:
        if chunk["type"] != "explanation":
            result.append(chunk)
            continue
        simple_text = chunk["text"]
        idx = chunk["exp_index"]
        override = section_translations[idx] if idx < len(section_translations) else {}
        result.append({
            "type": "explanation",
            "simple": simple_text,
            "technical": override.get("technical", simple_text),
            "hinglish": override.get("hinglish", simple_text),
        })
    return result

BANNER_RE = re.compile(
    r"^# ={80,}\n((?:# .*\n)+?)# ={80,}\n",
    re.MULTILINE,
)
SECTION_CALL_RE = re.compile(r'^section\("([^"]+)"\)', re.MULTILINE)
QUESTION_NUM_RE = re.compile(r"QUESTION\s+(\d+)", re.IGNORECASE)
DOCSTRING_RE = re.compile(r'^"""(.*?)"""', re.DOTALL)


def clean_comment_block(raw_title_lines):
    """Turns a run of '# text' comment lines (as captured by BANNER_RE's
    inner group) into one clean, joined string, e.g. for a multi-line
    QUESTION banner title."""
    lines = [l[2:] if l.startswith("# ") else l[1:] for l in raw_title_lines.strip("\n").split("\n")]
    return " ".join(l.strip() for l in lines if l.strip())


def split_into_zones(code_text):
    """Returns an ordered list of zones:
       [{"title": str_or_None, "content_start": int, "end": int}, ...]
    "title" is None for the very first (pre-banner) zone. "content_start"
    points PAST the banner's own "====.../title/====..." lines, so the
    banner's decorative ASCII-art text never leaks into the actual code
    we show (the banner's title is already shown separately as the
    section heading)."""
    banners = list(BANNER_RE.finditer(code_text))
    zones = []
    if not banners:
        return [{"title": None, "content_start": 0, "end": len(code_text)}]

    zones.append({"title": None, "content_start": 0, "end": banners[0].start()})
    for i, m in enumerate(banners):
        title = clean_comment_block(m.group(1))
        content_start = m.end()
        end = banners[i + 1].start() if i + 1 < len(banners) else len(code_text)
        zones.append({"title": title, "content_start": content_start, "end": end})
    return zones


def group_zones(zones, code_text):
    """Groups the raw banner zones into logical groups: setup / question N / wrapup.
    Returns an ordered list of {"kind", "number", "title", "code"} dicts."""
    groups = []
    current = None

    for zone in zones:
        title = zone["title"]
        text = code_text[zone["content_start"]:zone["end"]]
        qnum_match = QUESTION_NUM_RE.search(title) if title else None

        if qnum_match:
            qnum = int(qnum_match.group(1))
            if current and current["kind"] == "question" and current["number"] == qnum:
                current["code"] += text
            else:
                current = {"kind": "question", "number": qnum, "title": title, "code": text}
                groups.append(current)
        else:
            # Non-question zone: pre-banner prelude, a leading "LOADING..."
            # banner, or a trailing "SAVING..." banner.
            if not any(g["kind"] == "question" for g in groups):
                # We haven't hit Question 1 yet -> this is part of Setup.
                if current and current["kind"] == "setup":
                    current["code"] += text
                else:
                    current = {"kind": "setup", "number": None, "title": title, "code": text}
                    groups.append(current)
            else:
                # We're past the last question -> this is the wrap-up.
                if current and current["kind"] == "wrapup":
                    current["code"] += text
                else:
                    current = {"kind": "wrapup", "number": None, "title": title, "code": text}
                    groups.append(current)
    return groups


def code_to_chunks(code_text):
    """Splits a chunk of Python source into alternating
    {"type": "explanation"|"code", "text": ...} blocks, by grouping
    consecutive '#'-comment lines apart from consecutive real code lines.
    Each "explanation" chunk also gets an "exp_index" (0, 1, 2, ...) - its
    position among ONLY the explanation chunks in this code block, in
    order. This index is the stable key used to attach the hand-written
    Technical/Hinglish rewrites from lab_explanations_i18n.py to the right
    explanation chunk (the "Simple" style is always this auto-extracted
    text itself - zero extra authoring needed for that one style)."""
    lines = code_text.split("\n")
    chunks = []
    current_type = None
    current_lines = []
    exp_counter = [0]

    def line_text(l):
        stripped = l.strip()
        t = stripped[2:] if stripped.startswith("# ") else stripped.lstrip("#")
        return t.strip()

    def flush():
        nonlocal current_lines, current_type
        if current_type == "explanation":
            # Turn the comment run into paragraphs, split on blank "#"
            # lines AND on decorative "# ----" divider lines (both act
            # as a paragraph break - a divider that is silently
            # dropped instead of treated as a break would otherwise
            # glue the text before it and after it into one run-on
            # paragraph).
            paragraphs, para = [], []
            exp_lines = current_lines
            n = len(exp_lines)
            i = 0
            while i < n:
                text = line_text(exp_lines[i])
                is_divider = bool(re.fullmatch(r"-{5,}", text))

                if is_divider:
                    # Look ahead for a "# ----/# TITLE/# ----" 3-line
                    # heading block (used for banner-style sub-section
                    # titles inside a question, e.g. "STEP 0: ..." or
                    # "1a) SCATTER PLOT: ...").
                    if i + 2 < n:
                        mid = line_text(exp_lines[i+1])
                        after = line_text(exp_lines[i+2])
                        if mid and not re.fullmatch(r"-{5,}", mid) and re.fullmatch(r"-{5,}", after):
                            if para:
                                paragraphs.append(" ".join(para)); para = []
                            paragraphs.append("@@" + mid + "@@")
                            i += 3
                            continue
                    # A plain, standalone divider -> just a paragraph break.
                    if para:
                        paragraphs.append(" ".join(para)); para = []
                    i += 1
                    continue

                # A single-line mini-heading like '# --- Handling "Age" ---'
                # should be its own standalone (bolded) paragraph, not
                # merged into the sentence that follows it.
                heading_match = re.fullmatch(r"-{2,}\s*(.+?)\s*-{2,}", text)
                if heading_match:
                    if para:
                        paragraphs.append(" ".join(para)); para = []
                    paragraphs.append("@@" + heading_match.group(1) + "@@")
                    i += 1
                    continue

                if not text:
                    if para:
                        paragraphs.append(" ".join(para)); para = []
                else:
                    para.append(text)
                i += 1
            if para:
                paragraphs.append(" ".join(para))
            joined = "\n\n".join(p for p in paragraphs if p.strip())
            if joined.strip():
                chunks.append({"type": "explanation", "text": joined, "exp_index": exp_counter[0]})
                exp_counter[0] += 1
        elif current_type == "code":
            block = "\n".join(current_lines).strip("\n")
            if block.strip():
                chunks.append({"type": "code", "text": block})
        current_lines = []

    for line in lines:
        stripped = line.strip()
        is_comment = stripped.startswith("#")
        line_type = "explanation" if is_comment else "code"
        # Blank lines: keep them attached to whichever block is currently open,
        # so multi-line code blocks don't get needlessly fragmented.
        if not stripped:
            if current_lines:
                current_lines.append(line)
            continue
        if line_type != current_type:
            flush()
            current_type = line_type
        current_lines.append(line)
    flush()
    return chunks


def load_output_map(output_text):
    """Parses a captured run_output.txt into {section_title: body_text}."""
    delim = re.compile(r"\n=+\n(.+)\n=+\n")
    matches = list(delim.finditer(output_text))
    mapping = {}
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        body_start = m.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(output_text)
        mapping[title] = output_text[body_start:body_end].strip("\n")
    return mapping


def group_output(group_code, output_map):
    titles_in_order = SECTION_CALL_RE.findall(group_code)
    pieces = [output_map[t] for t in titles_in_order if t in output_map]
    return "\n\n".join(pieces)


def find_plots_for_group(plots_dir, group):
    """Finds plot PNGs whose filename starts with this question's number
    (e.g. '1a_...', '1b_...', '1_...' all match question number 1)."""
    if group["kind"] != "question" or not os.path.isdir(plots_dir):
        return []
    number = group["number"]
    found = []
    for path in sorted(glob.glob(os.path.join(plots_dir, "*.png"))):
        fname = os.path.basename(path)
        m = re.match(r"^(\d+)", fname)
        if m and int(m.group(1)) == number:
            found.append(path)
    return found


def encode_image(path):
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return "data:image/png;base64," + b64


def humanize_group_title(group):
    if group["kind"] == "setup":
        return "Setup: Loading the Dataset"
    if group["kind"] == "wrapup":
        return "Saving Your Results"
    # group["title"] is the raw, multi-line assignment question text pulled
    # straight from the code's own banner comment, e.g.
    # "QUESTION 2: Identify the number and percentage of missing values in
    # each column, and handle missing values using a suitable technique."
    # We keep it close to verbatim (it IS the assignment's own wording),
    # just trimming the leading "QUESTION N:" since we show that separately.
    text = group["title"]
    text = re.sub(r"^QUESTION\s+\d+\s*:\s*", "", text, flags=re.IGNORECASE)
    return text


def build_assignment(folder_path, num):
    py_files = glob.glob(os.path.join(folder_path, f"lab_assignment_{num}.py"))
    if not py_files:
        return None
    py_path = py_files[0]
    code_text = open(py_path, encoding="utf-8").read()

    output_path = os.path.join(folder_path, "run_output.txt")
    output_text = open(output_path, encoding="utf-8").read() if os.path.exists(output_path) else ""
    output_map = load_output_map(output_text)

    docstring_match = DOCSTRING_RE.match(code_text)
    intro_raw = docstring_match.group(1) if docstring_match else ""
    code_after_docstring = code_text[docstring_match.end():] if docstring_match else code_text

    zones = split_into_zones(code_after_docstring)
    groups = group_zones(zones, code_after_docstring)

    plots_dir = os.path.join(folder_path, "plots")

    sections = []
    for group in groups:
        section_id = f"{group['kind']}-{group['number']}" if group["number"] else group["kind"]
        chunks = code_to_chunks(group["code"])
        chunks = attach_explanation_styles(chunks, num, section_id)
        output_str = group_output(group["code"], output_map)
        plot_paths = find_plots_for_group(plots_dir, group)
        plots = [
            {"filename": os.path.basename(p), "data_uri": encode_image(p)}
            for p in plot_paths
        ]
        sections.append({
            "id": section_id,
            "kind": group["kind"],
            "number": group["number"],
            "label": humanize_group_title(group),
            "chunks": chunks,
            "output": output_str,
            "plots": plots,
        })

    # Figure out which dataset file this assignment reads, just by scanning
    # for the first .csv filename literal mentioned in the code, so the UI
    # can show an honest "Dataset used: ..." badge without us hand-typing it.
    dataset_match = re.search(r'"([^"/]+\.csv)"', code_text)
    dataset_name = dataset_match.group(1) if dataset_match else "Titanic-Dataset.csv"

    title_match = re.search(r"LAB ASSIGNMENT (\d+) - (.+)", intro_raw)
    title = f"Lab Assignment {num}"
    subtitle = title_match.group(2).strip() if title_match else ""

    # Strip the leading "====.../ LAB ASSIGNMENT N - .../ ====..." banner
    # from the intro text before handing it to the site - the page already
    # shows this exact title as its own <h1>, so repeating it as the first
    # paragraph of the intro would just be noisy duplication.
    intro_clean = re.sub(
        r"^\s*={3,}\s*\n\s*LAB ASSIGNMENT \d+ - .+\n\s*={3,}\s*\n",
        "",
        intro_raw.strip(),
    )

    return {
        "num": num,
        "title": title,
        "subtitle": subtitle,
        "dataset": dataset_name,
        "intro": intro_clean.strip(),
        "sections": sections,
    }


def main():
    assignment_dirs = sorted(
        glob.glob(os.path.join(ROOT, "Lab Assignment *")),
        key=lambda p: int(re.search(r"Lab Assignment (\d+)", p).group(1)),
    )

    assignments = []
    for d in assignment_dirs:
        num = int(re.search(r"Lab Assignment (\d+)", d).group(1))
        assignment = build_assignment(d, num)
        if assignment:
            assignments.append(assignment)

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "labs_content.js")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("window.LAB_ASSIGNMENTS = ")
        json.dump(assignments, f, ensure_ascii=False)
        f.write(";\n")

    total_questions = sum(
        len([s for s in a["sections"] if s["kind"] == "question"]) for a in assignments
    )
    print(f"Lab Assignments: {len(assignments)}, Questions: {total_questions}")
    print("Wrote", out_path)


if __name__ == "__main__":
    main()
