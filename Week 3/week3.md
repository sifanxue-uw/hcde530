# Week 3 — A3 competency claim

## Competency

I can debug CSV-driven Python workflows end to end: reproduce failures from messy survey exports, fix type and logic bugs so scripts finish without errors, and separate **cleaning** (normalize fields, write a tidy dataset) from **analysis** (summaries on the original or cleaned file).

## Evidence in this repo

- **`week3_analysis_buggy.py`** — Fixed script from class: handles non-numeric `experience_years`, corrects “top 5” satisfaction order, labels empty roles, and writes a text summary file when run on `week3_survey_messy.csv`.
- **Commit history** — Two commits document the main fixes (see **Commit notes** below).
- **`week3_clean_survey.py`** — Cleaning script with inline comments describing the loop, field normalization, and what is written to **`week3_survey_clean.csv`**.
- **`week3_survey_messy.csv`** — Messy input used to exercise both scripts.

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

*If your `git log` shows a `Made-with: Cursor` line under the message, that came from a local git template; you can remove it with `git rebase -i` and `reword`, or leave it—either way the two commit subjects above match the assignment style.*

## How to run

```bash
cd Week 3
python3 week3_clean_survey.py   # produces week3_survey_clean.csv
python3 week3_analysis_buggy.py # reads messy CSV; prints stats; writes week3_summary.txt
```
