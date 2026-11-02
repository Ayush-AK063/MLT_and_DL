"""
Generates site/netlify/functions/chat-data.json for the "Ask MLT AI" chatbot backend.

This does NOT re-read the lecture .md files or lab .py scripts. It re-reads the
already-generated site/content.js and site/labs_content.js (the same data the
static site itself uses) and repackages it into a lean, plain-text JSON file
that the Netlify function (site/netlify/functions/chat.js) loads at cold start.
This keeps a single source of truth: content.js/labs_content.js stay the only
place lecture/lab data is derived from markdown/scripts.

The output has two purposes for the chatbot's system prompt:
  1. A compact "index" of every lecture topic and every lab question (id + title
     only) that is cheap enough to embed in full in every request, so the model
     always knows the full breadth of the course without a tool call.
  2. A "topics" / "lab_sections" lookup keyed by a short id, used by the
     get_topic / get_lab_section function-tools the model calls on demand to
     pull in the FULL text (all three explanation styles) for grounding an
     answer, instead of stuffing ~190k tokens of notes into every request.

Run with: python3 build_chat_data.py   (stdlib only, no venv needed)
"""
import re
import os
import json
import html as html_module

ROOT = "/Users/etech/Desktop/MLT_&_DL/MLT_Python"
SITE_DIR = os.path.join(ROOT, "site")
OUT_PATH = os.path.join(SITE_DIR, "netlify", "functions", "chat-data.json")

TAG_RE = re.compile(r"<[^>]+>")


def strip_html(s):
    text = TAG_RE.sub(" ", s or "")
    text = html_module.unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return text.strip()


def load_window_json(path, varname):
    raw = open(path, encoding="utf-8").read()
    prefix = f"window.{varname} = "
    assert raw.startswith(prefix), f"{path} doesn't start with {prefix!r}"
    body = raw[len(prefix):].rstrip()
    if body.endswith(";"):
        body = body[:-1]
    return json.loads(body)


def build_lecture_data(lectures):
    index = []
    topics = {}
    for lec in lectures:
        topic_entries = []
        for t in lec["topics"]:
            key = f"{lec['num']}-{t['id']}"
            topic_entries.append({"id": t["id"], "title": t["title"]})
            topics[key] = {
                "lecture_num": lec["num"],
                "lecture_title": lec["title"],
                "topic_title": t["title"],
                "source": t.get("source", ""),
                "sections": [
                    {"heading": sec["heading"], "text": strip_html(sec["html"])}
                    for sec in t.get("sections", [])
                ],
            }
        index.append({
            "num": lec["num"],
            "label": lec.get("label", f"Lecture {lec['num']}"),
            "title": lec["title"],
            "subtitle": lec.get("subtitle", ""),
            "topics": topic_entries,
        })
    return index, topics


def section_label(s):
    if s["kind"] == "setup":
        return "Setup"
    if s["kind"] == "wrapup":
        return "Saving Results"
    return f"Question {s['number']}" + (f": {s['label']}" if s.get("label") else "")


def chunk_text(chunk, style="technical"):
    if chunk["type"] == "explanation":
        text = chunk.get(style) or chunk.get("simple") or chunk.get("text") or ""
        return text.replace("@@", "")
    return "```python\n" + chunk.get("text", "") + "\n```"


def build_lab_data(labs):
    index = []
    lab_sections = {}
    for lab in labs:
        section_entries = []
        for s in lab["sections"]:
            section_entries.append({
                "id": s["id"], "kind": s["kind"], "number": s.get("number"),
                "label": s.get("label", ""),
            })
            key = f"lab-{lab['num']}-{s['id']}"
            body_parts = [chunk_text(c) for c in s.get("chunks", [])]
            text = "\n\n".join(p for p in body_parts if p.strip())
            if s.get("output"):
                text += "\n\n--- Captured terminal output for this section ---\n" + s["output"]
            lab_sections[key] = {
                "lab_num": lab["num"],
                "label": section_label(s),
                "text": text,
            }
        index.append({
            "num": lab["num"],
            "title": lab["title"],
            "subtitle": lab.get("subtitle", ""),
            "dataset": lab.get("dataset", ""),
            "sections": section_entries,
        })
    return index, lab_sections


def main():
    lectures = load_window_json(os.path.join(SITE_DIR, "content.js"), "LECTURES")
    labs = load_window_json(os.path.join(SITE_DIR, "labs_content.js"), "LAB_ASSIGNMENTS")

    lectures_index, topics = build_lecture_data(lectures)
    labs_index, lab_sections = build_lab_data(labs)

    out = {
        "lectures_index": lectures_index,
        "topics": topics,
        "labs_index": labs_index,
        "lab_sections": lab_sections,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)

    total_topics = sum(len(l["topics"]) for l in lectures_index)
    total_lab_sections = sum(len(l["sections"]) for l in labs_index)
    print(f"Lectures: {len(lectures_index)}, Topics: {total_topics}")
    print(f"Lab Assignments: {len(labs_index)}, Sections: {total_lab_sections}")
    print("Wrote", OUT_PATH, f"({os.path.getsize(OUT_PATH)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
