# Week 3 — A3 competency claim

## Competency: debugging messy survey data with clear version history

### What this competency means to me

For me, this week is partly about **attention to detail** when correcting errors: a wrong data type in one cell, a default `sort` that quietly flips the meaning of “top five,” or an empty field that shows up as a blank label in a summary. Those issues are small on their own, but they change the story the script tells, so catching them matters.

I also care about **using several commits while debugging** as a form of **version control**. Each commit is a checkpoint with a message that says what was wrong and what I changed, so the history reads like a short log of the investigation instead of one vague “fixed stuff” step.

### What I did this week (evidence)

- **`week3_analysis_buggy.py`** — Diagnosed and fixed the class script so it runs on `week3_survey_messy.csv` without errors: non-numeric `experience_years`, wrong satisfaction ranking, empty `role` labels, and a written summary file.
- **`week3_clean_survey.py`** — Extended the cleaning idea with inline `#` comments: what the loop does, how fields are normalized, and what gets written to **`week3_survey_clean.csv`**.
- **`week3_survey_messy.csv`** — Messy input used for both pipelines.
- **Git history** — Two separate commits, each tied to a concrete bug (see **Commit notes** below), so the debugging process is visible in the repo.

### How multiple commits support debugging for me

Splitting fixes into **two commits** matched how I actually worked: first unblock the crash (`ValueError` on `fifteen`), then fix logic and output (sort direction, `Unknown` role, summary file, cleaner). If something regressed, I could compare states commit by commit instead of rereading one giant diff. That is the version-control habit I want to practice: **small, named steps** instead of one opaque push.

### What I learned about reading or writing code

Reading tracebacks and scanning the CSV row that triggered them taught me to connect **runtime errors** to **specific cells**, not only to “Python is broken.” Writing the cleaning script also made me think about **where** normalization should live (one place that writes a clean file) versus **what** the analysis script should assume.

### One concrete example (file, snippet, or decision)

In **`week3_analysis_buggy.py`**, the satisfaction “top five” bug was subtle: the code sorted ascending and sliced the first five, which listed the **lowest** scores. Switching to `reverse=True` was a one-word change with a big meaning difference—exactly the kind of detail I want to catch by reading output and questioning whether it matches the question we asked of the data.

### What I want to improve next

I want to get faster at **sanity-checking outputs** (totals, extremes, empty categories) before I call a script “done,” and at writing commit messages that stay specific even when I fix more than one line in a pass.

---

## Commit notes (A3 — two commits, one main bug each)

### Commit 1 — `9a770a2`

**Message:** `fix: ValueError parsing experience_years (non-numeric 'fifteen')`

**What was wrong:** The script used `int(row["experience_years"])`. One row (R009) stores years as the word `fifteen`, which raises `ValueError: invalid literal for int() with base 10: 'fifteen'`.

**What changed:** Added `parse_experience_years()` plus a small word map, and averaged only rows with a parseable value so the script completes past that column.

---

### Commit 2 (tip of `main` — run `git log -1 --oneline` to see current SHA)

**Message:** `fix: satisfaction top-5 used ascending sort; label empty roles as Unknown; write week3_summary.txt; add cleaning script and week3.md`

**What was wrong:** (1) `list.sort()` defaults to ascending order, so `[:5]` returned the five *lowest* satisfaction scores, not the highest. (2) An empty `role` produced a blank label in the role counts. (3) The rubric expects a clean output file from the fixed analysis.

**What changed:** Sort with `reverse=True` for true top five; treat empty role as `Unknown`; write `week3_summary.txt` with the printed summary; add `week3_clean_survey.py`, `week3_survey_clean.csv`, and this file.

---

*If your `git log` shows a `Made-with: Cursor` line under the message, that came from a local git template; you can remove it with `git rebase -i` and `reword`, or leave it.*

## How to run

```bash
cd Week 3
python3 week3_clean_survey.py   # produces week3_survey_clean.csv
python3 week3_analysis_buggy.py # reads messy CSV; prints stats; writes week3_summary.txt
```
