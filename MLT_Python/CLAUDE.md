# MLT_Python — Lecture Notes Workflow (ES514: Machine Learning Techniques)

This file is the standing playbook for turning a lecture PDF into notes in this repo. Read this before processing any new lecture — it captures the exact workflow established across Lectures 1–8 so every future lecture follows the same standard without needing to be re-explained.

## Project context

- Course: **ES514, Machine Learning Techniques** (ABV-IIITM Gwalior, Dr. Yashwant Singh Patel).
- The user is a **complete beginner** — no prior Python or ML/MLT knowledge. Every explanation must work for someone starting from zero.
- Folder layout:
  - `lectures/Lecture N/` — one folder per lecture, created fresh for each new PDF.
  - `Lab_assingments/` — separate, not part of this workflow.
- Source PDFs live in `~/Downloads/Lecture N <Title>.pdf` and are supplied by the user one at a time.

## The workflow, step by step

1. **Read the entire PDF, no exceptions.** Check the page count first (`pymupdf`/`fitz` via the venv at
   `/private/tmp/claude-501/.../scratchpad/venv` — see "Environment notes" below), then read the whole document, even if it's 40–60+ pages, in one or more `Read` calls. Nothing gets skipped, including handwritten annotations, worked examples, and footnote-style source citations on slides.
2. **Cross-check against prior lectures.** Recap slides often repeat earlier content verbatim (e.g., Lecture 7 slides 2–6 = Lecture 6 content word-for-word). Don't duplicate a full explanation that already exists — write a short recap-note file that links back to the earlier lecture's file (`[[filename]]` style reference) instead of re-explaining from scratch. Only write fresh notes for genuinely new content.
3. **Flag anomalies, don't silently absorb or silently drop them.** If a PDF contains slides that look unrelated to the course (e.g., Lecture 5's "European Spallation Source Tour" pages), say so explicitly to the user and explain the reasoning — but stay open to correction from a later lecture's recap (this happened once: Lecture 6's recap confirmed the ESS content *was* intentional, so the earlier flag was revised). When a correction like this happens, update the earlier lecture's README to reflect it.
4. **Do targeted web research to enrich, not to pad.** For each genuinely new topic (a named algorithm, a historical event, a technique), run 2–4 targeted `WebSearch` queries to add real depth beyond what the slides literally say (e.g., Deep Blue history, IQR outlier method, hot/cold deck imputation). Cite what was learned naturally in the technical explanation. Skip research for content that's already fully self-contained and mathematical (formulas + worked numbers don't need external sourcing).
5. **Verify every worked numeric example independently.** When a slide shows a formula plus a worked table of numbers (scaling methods, binning, Z-score, IQR, etc.), recompute it by hand/mentally or via a quick calculation to confirm the stated results — and note any inferred detail the slide didn't spell out (e.g., discovering the Z-score example used *sample* std-dev, not population; the Robust Scaler used linear-interpolation quartiles; Log Transformer used natural log, not log10). This has caught real ambiguities in the source slides.
6. **Structure notes as one Markdown file per topic**, not one giant file per lecture. A lecture typically produces 4–14 topic files depending on density (short conceptual lectures → fewer files; dense math-heavy lectures like Data Cleaning/Transformation → more files). Split at natural topic boundaries matching the slide deck's own section headers.
7. **Every topic file follows the same three-section template** (see "File template" below): Technical, Simple English, Hinglish. This is non-negotiable — it's the core deliverable the user asked for from the start.
8. **Write a `README.md` per lecture folder** — an index table (file → one-line topic description), a note on the "three styles" convention, and any flags/corrections/verification notes relevant to that lecture.
9. **No images, no PDFs — text-only `.md` files.** This was explicitly requested after an earlier experiment with embedding extracted PDF images and generating a combined PDF. Do not reintroduce images or binary attachments in the `.md` files unless the user asks again. (Starting with Lecture 10, the *site* — not the `.md` files — may show a slide's own graph/diagram recreated as hand-drawn inline SVG via `site/diagrams.js`; see "The website" section below. That's a display-layer addition, not a reversal of this rule — the note files themselves stay text-only.)
10. **After finishing a lecture, give a short summary** in chat: list of files created, one line each, plus anything worth flagging (corrections, verified math, anomalies). Don't paste full note content into the chat — the files are the deliverable.

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
Assume the reader knows nothing about ML or Python.>

---

## 3) Hinglish Explanation (Beginner-Friendly)

<Same content again, in Hinglish (Roman-script Hindi+English mix), for a reader who
knows zero Python/ML and is more comfortable thinking in Hindi. Match the technical
precision of section 1, just in a different language register.>
```

Rules for each section:
- All three sections must cover the **same information** — just at different registers of language, not different depth. A reader should be able to read only section 3 and still get the full picture.
- Worked math examples appear in full in section 1 (technical), and are re-explained step-by-step in sections 2 and 3, not just referenced.
- Use `[[Other_Topic_File_Name]]` to cross-reference related concepts, and say which lecture it's from if it's not the current one, e.g. `[[06_Course_Syllabus_Roadmap_and_Resources]] from Lecture 1`.

## Naming conventions

- Lecture folder: `lectures/Lecture N/` (capital L, space, number — matches existing folders 1–8).
- Topic files: `NN_Descriptive_Snake_Case_Title.md`, zero-padded two-digit prefix (`00_`, `01_`, …) in slide order.
- `00_` is reserved for a recap/continuity file when the lecture opens with a recap of the previous lecture (very common in this course).
- Index file: always `README.md`, always at the lecture folder root.

## The website (`site/`)

- All lecture notes are also published as a browsable static website in `site/` — a single-page
  app (`index.html` + `style.css` + `app.js`) with all lecture/topic content pre-rendered into
  `site/content.js` by `build_site.py` (project root). No framework, no build tool, no npm —
  pure static HTML/CSS/JS, deployable to Netlify by dragging the `site` folder onto
  https://app.netlify.com/drop (see `site/README-DEPLOY.md` for all deploy options).
- Features: sidebar with all lectures/topics, full-text search (⌘K), light/dark theme toggle,
  each topic shown as three tabs (Technical / Simple English / Hinglish), clickable
  cross-reference chips resolved from the `[[Topic_Id]]` links inside the notes, prev/next topic
  pager, and hash-based routing (`#/lecture/N/topic-id`) so every topic has a shareable URL and
  works as a plain static site with zero server-side logic.
- **Whenever lecture notes are added or edited, regenerate the site before telling the user it's
  ready to redeploy:**
  ```bash
  VENV=<the scratchpad venv from this session, or create a fresh one with:
        python3 -m venv .venv && .venv/bin/pip install markdown2>
  $VENV/bin/python3 /Users/etech/Desktop/MLT_&_DL/MLT_Python/build_site.py
  ```
  This overwrites `site/content.js` only — `index.html`, `style.css`, `app.js`, `netlify.toml`
  never need to change just because new lecture notes were added.
- If the site's design/behavior itself needs a change (new feature, restyle), edit
  `site/index.html` / `site/style.css` / `site/app.js` directly — those are hand-written, not
  generated.
- **`site/diagrams.js`** (hand-written, like `app.js`) holds hand-drawn, theme-aware **inline SVG**
  recreations of specific slide figures (graphs/scatter-plots/grids), keyed by
  `"<lectureNum>-<topicId>"` (topicId = the note filename without `.md`) → an array of
  `{caption, svg}` entries. `app.js`'s `renderTopic()` looks up `window.DIAGRAMS[...]` and renders
  any matches right under the topic heading, above the Technical/Simple/Hinglish tabs. This exists
  because the `.md` notes and `build_site.py`'s output must stay **text-only** (rule below), but a
  slide's own diagram is sometimes worth showing on the site specifically — so recreate it as SVG
  (never a screenshot/PNG) and add one more entry to this file; nothing else needs to change. Only
  add a diagram when it earns its place (a real graph/plot/grid from the slides), not for every
  topic.
- Markdown quirk handled by the generator: a bullet/numbered list immediately following a
  non-blank line (no blank line in between) needs a blank line inserted before it, or the
  `markdown2` renderer treats it as plain paragraph text instead of a list. `build_site.py`'s
  `ensure_blank_before_lists()` already patches this automatically — no need to reformat the
  source `.md` files for this reason.

### Ask MLT AI (chatbot, `site/netlify/functions/chat.js`)

- A chat page at `#/chat` in the site (nav link "🤖 Ask MLT AI" pinned at the top of the sidebar)
  lets the student ask free-form questions and get answers grounded in their own lecture/lab
  notes, enriched with live web research, with OpenAI's key held server-side.
- **Backend**: `site/netlify/functions/chat.js`, a Netlify Function (Node 18+, no npm
  dependencies — uses global `fetch`). It calls OpenAI's **Responses API**
  (`https://api.openai.com/v1/responses`) with a hosted `{"type": "web_search"}` tool (OpenAI runs
  the search itself server-side, no round trip needed) plus two custom function tools,
  `get_topic` and `get_lab_section`, that the model calls on demand to fetch the exact
  ground-truth text of one lecture topic or lab question (looked up by the
  `<lectureNum>-<topicId>` / `lab-<labNum>-<sectionId>` keys given in a full compact course index
  embedded in the system prompt). Multi-turn conversation state is chained via OpenAI's
  `previous_response_id`, not by resending full history from the client.
- **Data**: `site/netlify/functions/chat-data.json`, generated by `build_chat_data.py` (project
  root, stdlib-only, no venv needed) by re-reading the ALREADY-generated `site/content.js` and
  `site/labs_content.js` — never re-derives from the raw `.md`/`.py` sources directly, so there is
  still only one place lecture/lab data comes from. Regenerate it (`python3 build_chat_data.py`)
  any time `content.js`/`labs_content.js` change, same as the other two build scripts.
- **Frontend**: chat UI lives in `site/app.js` (`renderChat`, `sendChatMessage`,
  `renderMarkdownLite` for turning the model's markdown-ish reply into HTML) and
  `site/style.css` (`.chat-*` rules at the end of the file). Posts to `/api/chat`, which
  `site/netlify.toml` redirects to the function.
- **Required env var**: `OPENAI_API_KEY`, set in Netlify site settings (or `netlify env:set`) —
  **never** put it in any client-side file; a static site can't hide it. Optional `OPENAI_MODEL`
  (defaults to `gpt-4.1`).
- **Deploy caveat**: plain drag-and-drop to app.netlify.com/drop does **not** deploy the
  `netlify/functions/` folder — the chatbot needs `netlify deploy` via the CLI or a Git-linked
  site (Options B/C in `site/README-DEPLOY.md`). Drag-and-drop still works fine for everything
  else on the site; only the chat page's messages would fail.
- If the chatbot's own behavior needs a change (system prompt wording, tool logic, model), edit
  `site/netlify/functions/chat.js` directly — it's hand-written, like `app.js`.

### Lab Assignments mode (`site/labs_content.js`, generated by `build_labs.py`)

- The same site also has a "Lab Assignments" mode (separate sidebar section, `#/lab/N` and
  `#/lab/N/section-id` routes) that browses the fully-solved, heavily-commented scripts in
  `Lab_assingments/Lab Assignment N/lab_assignment_N.py` — each question shown as alternating
  explanation/code cards (parsed straight from the script's own `#` comments vs real code lines),
  the exact captured terminal output for that question, and any plot PNGs it produced, embedded
  as base64 data URIs (no extra asset folder to keep in sync).
- **This is Phase 1 (static browsing) of a larger, explicitly multi-phase plan the user asked
  for** — do not silently treat it as finished. The "Run this code" button is intentionally
  disabled with a "coming in a future update" note. Later phases (only build when the user asks
  to continue): Phase 2 = live in-browser Python execution via Pyodide for the pre-written
  assignment code; Phase 3 = a "Test mode" where the user uploads their own CSV and writes their
  own code in an in-page editor and runs it the same way; Phase 4 = an AI explain/critique feature
  for arbitrary user-submitted code — **do not wire this to a client-side OpenAI key**, a static
  page can't hide it (viewable in DevTools) and the user has both an OpenAI key and is open to a
  backend (mentioned Vercel/Netlify Functions) if one turns out to be needed; the safer options are
  a small serverless function holding the key server-side, or (if ever published as a Claude
  Artifact instead of/alongside the Netlify site) the Artifact platform's built-in "ask Claude"
  capability, which needs no key at all — load the `artifact-capabilities` skill before building
  that path.
- **Whenever a lab assignment script or its captured output changes, regenerate before telling
  the user it's ready to redeploy** (same venv as `build_site.py`; also re-run the assignment
  script itself first with output redirected to `run_output.txt` in its own folder if the code
  changed, so the captured output stays in sync with the code):
  ```bash
  $VENV/bin/python3 /Users/etech/Desktop/MLT_&_DL/MLT_Python/build_labs.py
  ```
  This overwrites `site/labs_content.js` only. `build_labs.py` splits each script on its own
  `# ====...====` / `# QUESTION N: ...` / `# ====...====` banner comments (already used
  consistently in every `lab_assignment_N.py`) — keep using that exact banner convention (and a
  `plots/<question-number><optional-letter>_description.png` naming convention for any saved
  matplotlib figures) in any future lab assignment script so it parses the same way with zero
  extra config.

## Environment notes (for reading PDFs and doing quick calculations)

- `Read` on a PDF path returns full page content (text + rendered images) without needing extra tools for lectures under ~40 pages in one call; for very large PDFs, check page count first with the venv Python + PyMuPDF snippet below and read in one call if possible (it has worked up to 66 pages in a single `Read`).
- A working Python venv with `pymupdf`, `markdown2`, `fpdf2`, `Pillow` exists at:
  `/private/tmp/claude-501/-Users-etech-Desktop-MLT-Python/<session-id>/scratchpad/venv`
  — the session ID changes per session, so re-create the venv if it's missing (`python3 -m venv .../scratchpad/venv && .../venv/bin/pip install pymupdf`). Only needed for page-count checks or ad hoc verification scripts now that the PDF→image and PDF→combined-notes workflows have been retired per user request (see rule 9 above).
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

- **Images**: tried once (extracting PDF images, embedding in `.md`), then explicitly reverted — user wants text-only markdown. Do not re-add images unless asked.
- **PDF export**: tried once (building a combined PDF via fpdf2 for WhatsApp-sharing), then explicitly reverted for the same reason as images — user wants only the per-topic `.md` files, nothing else generated alongside them.
- **Anomalous content**: flag clearly rather than guessing silently; be ready to revise a flag if a later lecture's recap contradicts it (happened with the ESS Tour content between Lectures 5 and 6).
- **Depth over brevity**: when a lecture is large (e.g., Lecture 3 at 66 slides, Lecture 6 at 43 slides), the instruction was explicitly "kuch bhi chutna nahi chahiye" (nothing should be missed) — err toward more topic files and full coverage, not compression.
- **Worked math**: always verify numerically. This has repeatedly caught non-obvious details the slides didn't state explicitly (sample vs population std-dev, natural vs base-10 log, percentile interpolation method).

## When a new lecture arrives

1. Confirm the PDF path the user gives you.
2. Check page count, then read it in full.
3. Skim for: (a) recap slides referencing earlier lectures, (b) any content that looks out of place, (c) worked numeric examples needing verification, (d) topics warranting web research.
4. Create `lectures/Lecture N/` and write topic files per the template above, in slide order.
5. Write `README.md` for the lecture.
6. Report back concisely: files created + any flags/corrections/verifications worth mentioning.

Do not ask the user to re-confirm this workflow each time — just follow it. Only check in if something genuinely unusual comes up (e.g., a PDF that doesn't match the expected course, or content that seems impossible to reconcile with prior lectures).
