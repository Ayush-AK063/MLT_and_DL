# DL_Python — Lecture Notes Workflow (ES532: Introduction to Deep Learning)

This file is the standing playbook for turning a lecture PDF into notes in this repo. Read this
before processing any new lecture. It mirrors the exact workflow used in the sibling project
`../MLT_Python` (see that folder's own `CLAUDE.md` if anything here is ambiguous) so both course
note-sites behave identically, just with separate content and a separate deploy.

## Project context

- Course: **ES532, Introduction to Deep Learning** (ABV-IIITM Gwalior, Dr. Yashwant Singh Patel —
  confirmed from the Lecture 8 PDF's title slide on 2026-09-20; same instructor/institute as the
  sibling `MLT_Python` project's ES514 course). `site/index.html`'s `<title>`/brand text has been
  updated to match. **`site/netlify/functions/chat.js`'s system prompt was deliberately left as
  generic placeholder text** — the chatbot is currently disabled (see the dedicated section below)
  and the user explicitly asked not to update it while it's off; only fill in the real course
  code/instructor there if/when the chatbot is re-enabled.
- The user is a **complete beginner** — no prior Python or ML/DL knowledge. Every explanation must
  work for someone starting from zero. (Some DL topics will build on ML fundamentals already
  covered in `../MLT_Python/lectures/` — it's fine to cross-reference those files with a
  `[[topic-file-name]] from MLT Lecture N` style note when a concept was already explained there,
  the same cross-lecture-reference convention used within MLT_Python itself. Only do this when the
  concept is genuinely identical, not just related.)
- **Lecture numbering (updated 2026-10-05):** `lectures/Lecture 0/` is Ruder's gradient-descent overview paper (a standalone reference reading, originally filed as "Lecture 1"); `Lecture 1`–`Lecture 13` follow the real course deck numbers (Lectures 1–7 and 13 were added 2026-10-05; 8–12 earlier). The two repeated-slide overlaps (L1↔L2 representation slides, L2↔L3 perceptron slides) are written up once and linked from `00_/01_Recap` files. Source PDFs named `... (1).pdf` in ~/Downloads are byte-different copies with identical text — don't re-process them. PDFs titled "ES514 / Machine Learning Techniques" belong to `../MLT_Python`, not here.
- **Lectures were arriving out of order** (confirmed by the user on 2026-09-20): they have Lectures
  8–12 in hand and Lectures 2–7 not yet. Each lecture folder is created under its **own real
  lecture number** as it arrives — `lectures/Lecture 8/`, `lectures/Lecture 9/`, etc. — never
  renumbered or renamed to fill gaps. `build_site.py` already sorts lecture folders numerically
  by whatever `Lecture N` number it finds (see its `lecture_dirs = sorted(...)` line), so the site
  will render correctly regardless of which numbers exist or in what order they were added; gaps
  (missing Lecture 2–7 folders) are expected and not a bug. When a lecture whose number is
  *earlier* than one already on the site arrives later (e.g. Lecture 3 arrives after Lecture 8 is
  already up), check its recap slides against whichever *later* lecture already has notes, not
  just against other early lectures, since the recap may reference content that's already written.
  One lecture at a time, per the user's explicit instruction — wait for the next PDF rather than
  asking for several up front.
- Folder layout (identical to MLT_Python):
  - `lectures/Lecture N/` — one folder per lecture, created fresh for each new PDF.
  - `Lab_assingments/` — separate, not part of this note-writing workflow (same spelling kept
    intentionally, matching the sibling project, in case any tooling ever assumes it).
- Source PDFs will be supplied by the user one at a time (path TBD — ask if not given as
  `~/Downloads/...`).

## The workflow, step by step

1. **Read the entire PDF, no exceptions.** Check the page count first (`pymupdf`/`fitz` via a
   scratchpad venv — see "Environment notes" below), then read the whole document, even if it's
   40–60+ pages, in one or more `Read` calls. Nothing gets skipped, including handwritten
   annotations, worked examples, and footnote-style source citations on slides.
2. **Cross-check against prior lectures** (both this course's own earlier lectures AND, where
   relevant, `../MLT_Python/lectures/` for foundational ML concepts DL builds on — e.g. gradient
   descent, overfitting, train/val/test splits). Don't duplicate a full explanation that already
   exists — write a short recap-note file that links back to the earlier file (`[[filename]]`
   style reference, adding `from MLT Lecture N` when the source is the sibling project) instead of
   re-explaining from scratch. Only write fresh notes for genuinely new content.
3. **Flag anomalies, don't silently absorb or silently drop them.** If a PDF contains slides that
   look unrelated to the course, say so explicitly to the user and explain the reasoning — but
   stay open to correction from a later lecture's recap.
4. **Do targeted web research to enrich, not to pad.** For each genuinely new topic (a named
   architecture, a historical milestone, a technique), run 2–4 targeted `WebSearch` queries to add
   real depth beyond what the slides literally say. Cite what was learned naturally in the
   technical explanation. Skip research for content that's already fully self-contained and
   mathematical (formulas + worked numbers don't need external sourcing).
5. **Verify every worked numeric example independently.** When a slide shows a formula plus a
   worked example (forward pass, loss computation, backprop gradient, convolution output size,
   etc.), recompute it by hand/mentally or via a quick calculation to confirm the stated results —
   and note any inferred detail the slide didn't spell out.
6. **Structure notes as one Markdown file per topic**, not one giant file per lecture. A lecture
   typically produces 4–14 topic files depending on density. Split at natural topic boundaries
   matching the slide deck's own section headers.
7. **Every topic file follows the same three-section template** (see "File template" below):
   Technical, Simple English, Hinglish. This is non-negotiable.
8. **Write a `README.md` per lecture folder** — an index table (file → one-line topic
   description), a note on the "three styles" convention, and any flags/corrections/verification
   notes relevant to that lecture.
9. **No images, no PDFs — text-only `.md` files.** Same rule as MLT_Python. A slide's own
   graph/diagram may be recreated as a hand-drawn inline SVG in `site/diagrams.js` instead (see
   "The website" below) — that's a display-layer addition, not a reversal of this rule.
10. **After finishing a lecture, give a short summary** in chat: list of files created, one line
    each, plus anything worth flagging. Don't paste full note content into the chat — the files
    are the deliverable.

## File template (apply to every topic file)

```markdown
# Topic N: <Topic Title>

Source: Lecture X, slides A–B (<slide titles/section names>). Enriched with web research (<sources>, only if research was done).

---

## 1) Technical Explanation

<Precise, terminology-correct explanation. Quote the slide's own definitions where useful.
Include full formulas, worked numeric examples (verified), and cross-references to
related topics in other lectures using [[topic-file-name]] style links.>

---

## 2) Simple English Explanation

<Same content, but in plain English with everyday analogies. No jargon left unexplained.
Assume the reader knows nothing about ML/DL or Python.>

---

## 3) Hinglish Explanation (Beginner-Friendly)

<Same content again, in Hinglish (Roman-script Hindi+English mix), for a reader who
knows zero Python/DL and is more comfortable thinking in Hindi. Match the technical
precision of section 1, just in a different language register.>
```

Rules for each section:
- All three sections must cover the **same information** — just at different registers of
  language, not different depth. A reader should be able to read only section 3 and still get the
  full picture.
- Worked math examples appear in full in section 1 (technical), and are re-explained step-by-step
  in sections 2 and 3, not just referenced.
- Use `[[Other_Topic_File_Name]]` to cross-reference related concepts, and say which lecture (and,
  if it's the sibling ML course, which project) it's from, e.g.
  `[[03_Bias_and_Variance]] from MLT Lecture 9`.

## Naming conventions

- Lecture folder: `lectures/Lecture N/` (capital L, space, number).
- Topic files: `NN_Descriptive_Snake_Case_Title.md`, zero-padded two-digit prefix (`00_`, `01_`,
  …) in slide order.
- `00_` is reserved for a recap/continuity file when the lecture opens with a recap of the
  previous lecture.
- Index file: always `README.md`, always at the lecture folder root.

## The website (`site/`)

- All lecture notes are also published as a browsable static website in `site/` — a single-page
  app (`index.html` + `style.css` + `app.js`) with all lecture/topic content pre-rendered into
  `site/content.js` by `build_site.py` (project root). No framework, no build tool, no npm —
  pure static HTML/CSS/JS, deployable to Netlify by dragging the `site` folder onto
  https://app.netlify.com/drop (see `site/README-DEPLOY.md` for all deploy options). This is a
  **separate site from MLT_Python's** — deploy it as its own Netlify site so the two courses stay
  independently shareable.
- Features (identical to MLT_Python's site): sidebar with all lectures/topics, full-text search
  (⌘K), light/dark theme toggle, each topic shown as three tabs (Technical / Simple English /
  Hinglish), clickable cross-reference chips resolved from the `[[Topic_Id]]` links inside the
  notes, prev/next topic pager, hash-based routing (`#/lecture/N/topic-id`), and a "Lab
  Assignments" browsing mode. The "Ask DL AI" chatbot page/nav-link exists in the code but is
  **currently commented out** in `site/app.js` (per the user's 2026-09-20 request — DL_Python
  doesn't need the chatbot yet, only lecture browsing) — see the dedicated section below before
  touching it.
- **Whenever lecture notes are added or edited, regenerate the site before telling the user it's
  ready to redeploy:**
  ```bash
  VENV=<a scratchpad venv with markdown2 installed>
  $VENV/bin/python3 "/Users/etech/Desktop/MLT_&_DL/DL_Python/build_site.py"
  ```
  This overwrites `site/content.js` only — `index.html`, `style.css`, `app.js`, `netlify.toml`
  never need to change just because new lecture notes were added.
- If the site's design/behavior itself needs a change (new feature, restyle), edit
  `site/index.html` / `site/style.css` / `site/app.js` directly — those are hand-written, not
  generated. Keep them in sync with MLT_Python's versions for anything that isn't
  course-specific, unless the user asks for the two sites to diverge in design.
- **`site/diagrams.js`** (hand-written, like `app.js`) holds hand-drawn, theme-aware **inline SVG**
  recreations of specific slide figures, keyed by `"<lectureNum>-<topicId>"` → an array of
  `{caption, svg}` entries (Lecture 0 has four entries so far, recreating the source paper's own
  figures). Add an entry only when a slide/figure genuinely earns its place (see MLT_Python's
  `site/diagrams.js`, or this project's own Lecture 1 entries, for the pattern to follow).
- Markdown quirk handled by the generator: a bullet/numbered list immediately following a
  non-blank line (no blank line in between) needs a blank line inserted before it, or the
  `markdown2` renderer treats it as plain paragraph text instead of a list. `build_site.py`'s
  `ensure_blank_before_lists()` already patches this automatically — no need to reformat the
  source `.md` files for this reason.
- The lecture-title parser in `build_site.py` expects a README's first line to look like
  `# Lecture N — Title` or `# Lecture N — Title (Subtitle)`, where a trailing `(...)` becomes the
  lecture's subtitle line on the site. Once the real course code is known, keep using this exact
  README heading format so parsing stays consistent with MLT_Python's convention.

### Ask DL AI (chatbot, `site/netlify/functions/chat.js`) — currently disabled

- **Status as of 2026-09-20: disabled on purpose, per explicit user request** ("abhi hme chat ki
  jarurat nhi hai... usko comment krke hta do... usko hme abhi update bhi nhi krna hai" — DL_Python
  doesn't need the chatbot right now; the site should just show lectures topic-wise). The nav link
  in `renderSidebar()` and the `#/chat` branch in `route()`, both in `site/app.js`, are commented
  out (not deleted) — the underlying `renderChat`/`sendChatMessage`/etc. functions and
  `site/netlify/functions/chat.js` are all still present untouched, just unreachable from the UI.
  **Do not regenerate `chat-data.json` or otherwise "keep the chatbot updated" as part of the
  normal per-lecture workflow** while it's in this state — only touch it again if the user
  explicitly asks to turn the chatbot back on.
- To re-enable later: uncomment the `chatLink` block near the top of `renderSidebar()` and the
  `else if(parts[0] === "chat")` branch in `route()` (both in `site/app.js`), and uncomment the
  auto-verify-on-load `fetch("/api/chat", ...)` block right after the `chatPassword` declaration.
  Then resume the earlier workflow: it's a chat page at `#/chat` that lets the student ask
  free-form questions grounded in their own lecture/lab notes plus live web research, OpenAI's key
  held server-side. Structurally identical to MLT_Python's chatbot — same Netlify Function, same
  Responses API + `web_search` + `get_topic`/`get_lab_section` tool pattern, same two-password
  persona gate (`123456` = normal, `042002` = personal) — only the system prompt text in `chat.js`
  is course-specific (currently generic "Deep Learning course" placeholders; tighten once the real
  course code/instructor are known, mirroring how MLT_Python's prompt names ES514 and its
  instructor explicitly).
- **Data**: `site/netlify/functions/chat-data.json`, generated by `build_chat_data.py` (project
  root, stdlib-only, no venv needed) by re-reading the ALREADY-generated `site/content.js` and
  `site/labs_content.js`. Regenerate it (`python3 build_chat_data.py`) any time `content.js`/
  `labs_content.js` change, same as the other two build scripts.
- **Frontend**: chat UI lives in `site/app.js` (`renderChat`, `sendChatMessage`,
  `renderMarkdownLite`) and `site/style.css` (`.chat-*` rules at the end of the file). Posts to
  `/api/chat`, which `site/netlify.toml` redirects to the function.
- **Required env var**: `OPENAI_API_KEY`, set in Netlify site settings for *this* site (separate
  from MLT_Python's Netlify site/env vars) — **never** put it in any client-side file. Optional
  `OPENAI_MODEL` (defaults to `gpt-4.1`).
- **Deploy caveat**: plain drag-and-drop to app.netlify.com/drop does **not** deploy the
  `netlify/functions/` folder — the chatbot needs `netlify deploy` via the CLI or a Git-linked
  site (Options B/C in `site/README-DEPLOY.md`). Drag-and-drop still works fine for everything
  else on the site; only the chat page's messages would fail.

### Lab Assignments mode (`site/labs_content.js`, generated by `build_labs.py`)

- Same mechanism as MLT_Python: a "Lab Assignments" sidebar section (`#/lab/N`,
  `#/lab/N/section-id`) that browses fully-solved, heavily-commented scripts in
  `Lab_assingments/Lab Assignment N/lab_assignment_N.py`, each question shown as alternating
  explanation/code cards, captured terminal output, and any plot PNGs embedded as base64 data
  URIs. Currently empty (no lab assignments yet) — only build this out when the user supplies lab
  scripts, following the exact same banner-comment convention
  (`# ====...====` / `# QUESTION N: ...` / `# ====...====`) documented in `build_labs.py`'s
  module docstring and `../MLT_Python/CLAUDE.md`.
- **Whenever a lab assignment script or its captured output changes, regenerate before telling
  the user it's ready to redeploy** (re-run the assignment script itself first with output
  redirected to `run_output.txt` in its own folder if the code changed):
  ```bash
  $VENV/bin/python3 "/Users/etech/Desktop/MLT_&_DL/DL_Python/build_labs.py"
  ```

## Environment notes (for reading PDFs and doing quick calculations)

- `Read` on a PDF path returns full page content (text + rendered images) without needing extra
  tools for lectures under ~40 pages in one call; for very large PDFs, check page count first with
  a venv Python + PyMuPDF snippet, and read in one call if possible.
- A working Python venv with `pymupdf`, `markdown2` is needed for page-count checks and running
  `build_site.py`/`build_labs.py` — create one in the session's scratchpad if missing:
  `python3 -m venv .../scratchpad/venv && .../venv/bin/pip install pymupdf markdown2`.
- Quick page-count check:
  ```bash
  VENV=/path/to/scratchpad/venv
  $VENV/bin/python3 -c "
  import fitz
  doc = fitz.open('/path/to/Lecture N.pdf')
  print('pages:', len(doc))
  "
  ```

## History of decisions (context so you don't re-litigate settled choices)

- This entire project was scaffolded from `../MLT_Python` on 2026-09-20, before any DL lecture
  content existed, specifically so the DL notes/site would look and behave identically to the MLT
  ones (same UI, same three-style template, same site features) while deploying as a fully
  separate site. All the "settled choices" from `../MLT_Python/CLAUDE.md`'s own history section
  (text-only `.md` notes, no PDF export, flag-don't-silently-absorb anomalies, verify all worked
  math, depth over brevity) apply here too — read that file if a decision here seems
  under-explained.
- Course code, instructor name, and institute are placeholders until the first lecture PDF
  confirms them — update this file plus `site/index.html` and `site/netlify/functions/chat.js`
  once known.

## When a new lecture arrives

1. Confirm the PDF path the user gives you.
2. Check page count, then read it in full.
3. Skim for: (a) recap slides referencing earlier lectures (this course's own, or foundational ML
   concepts from `../MLT_Python`), (b) any content that looks out of place, (c) worked numeric
   examples needing verification, (d) topics warranting web research.
4. Create `lectures/Lecture N/` and write topic files per the template above, in slide order.
5. Write `README.md` for the lecture.
6. Regenerate the site (`build_site.py`, plus `build_chat_data.py` if the chatbot should reflect
   the new content) before telling the user it's ready to redeploy.
7. Report back concisely: files created + any flags/corrections/verifications worth mentioning.

Do not ask the user to re-confirm this workflow each time — just follow it. Only check in if
something genuinely unusual comes up.
