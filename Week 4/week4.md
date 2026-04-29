# Week 4 — Competency Claim

## What I built (A4: API call + structured output)

I wrote a Python script **`seattle_bikes.py`** that calls a real public API: the **Seattle Open Data** (Socrata) endpoint for the **Fremont Bridge bicycle counters** (`https://data.seattle.gov/resource/65db-xm6k.json`). The script downloads JSON records, **extracts at least three fields** from each record, **prints** each record in a readable form, and **saves** the same data to **`seattle_bikes.csv`**.

This API is **different from the in-class demo API** (the course reviews endpoint). This dataset requires **no API key**; if I later use a key-based API, I will keep secrets in a **`.env`** file in the same folder as the script, load them with `os.environ.get(...)`, and never commit `.env` to GitHub (the repo root `.gitignore` ignores `.env`).

## How to run (for the reviewer)

From the `Week 4` folder:

```bash
python3 seattle_bikes.py
```

You should see one printed line per record (a small dictionary with three keys) and a final message that **`seattle_bikes.csv`** was written. The CSV is the structured artifact you can open in Excel, Google Sheets, or pandas.

## Competency claim

I can **find and read public API documentation**, **make an HTTP request from Python**, **parse JSON into native data structures**, **select fields that answer a question**, and **export structured results** (CSV) so the data is reusable and reviewable. I can also **document intent** with inline comments so another person (or future me) understands what the URL returns, what I extracted, and why those fields matter.

## HCD reflection (why this matters)

Bicycle counts on a major bridge are a **behavioral trace**: they show **when** and **how much** people move through a place, split by **direction** (northbound vs southbound). For human-centered design and urban mobility work, that kind of signal helps teams **ground decisions in observed patterns**—for example, peak times, imbalances between directions, or changes over time—instead of guessing. Pulling this data through an API and saving it as CSV is a small version of a common HCD-adjacent workflow: **integrate external evidence**, **structure it for analysis**, and **make it shareable** with collaborators who may not write code.
