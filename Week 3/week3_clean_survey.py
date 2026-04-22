import csv

"""
Read the messy Week 3 survey CSV, normalize key fields, and write a tidy CSV.
This is the cleaning pipeline; run it before analysis if you want a normalized dataset.
"""

# Same word-to-number map used in analysis when respondents type years as words.
_WORD_YEARS = {
    "fifteen": 15,
}

INPUT_CSV = "week3_survey_messy.csv"
OUTPUT_CSV = "week3_survey_clean.csv"


def parse_experience_years(raw):
    # Turn experience into an integer when possible; skip blank or unknown tokens.
    s = (raw or "").strip().lower()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        return _WORD_YEARS.get(s)


def clean_row(row):
    # Work on a copy so we do not mutate the original dict unexpectedly.
    out = dict(row)

    # Strip whitespace on every text field so "  UX Designer  " matches "UX Designer".
    for key in out:
        if out[key] is None:
            out[key] = ""
        elif isinstance(out[key], str):
            out[key] = out[key].strip()

    # Participant name: empty cells become a readable placeholder for reporting.
    if not out.get("participant_name"):
        out["participant_name"] = "Unknown"

    # Role and department: title case merges "ux researcher" with "UX Researcher".
    role = out.get("role") or ""
    out["role"] = role.title() if role else "Unknown"

    dept = out.get("department") or ""
    out["department"] = dept.title() if dept else ""

    # Primary tool: consistent capitalization (e.g. figma -> Figma).
    tool = out.get("primary_tool") or ""
    out["primary_tool"] = tool.title() if tool else ""

    # Replace experience with a numeric string, or empty if we cannot parse.
    years = parse_experience_years(out.get("experience_years"))
    out["experience_years"] = str(years) if years is not None else ""

    # Satisfaction must stay numeric for sorting; drop non-digits by leaving blank.
    score_raw = out.get("satisfaction_score") or ""
    if score_raw.strip().isdigit():
        out["satisfaction_score"] = str(int(score_raw.strip()))
    else:
        out["satisfaction_score"] = ""

    return out


def main():
    # Load all rows from the messy file into memory so we can write them in one pass.
    with open(INPUT_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = [clean_row(r) for r in reader]

    # Write cleaned rows to the output path using the same columns as the input.
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        # Each row is already normalized by clean_row(...).
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
