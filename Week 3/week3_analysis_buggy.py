import csv

# Messy exports sometimes store years as words; int() raised ValueError on values like "fifteen".
_WORD_YEARS = {
    "fifteen": 15,
}


def parse_experience_years(raw):
    """Return an int year, or None if blank or not parseable."""
    s = (raw or "").strip().lower()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        return _WORD_YEARS.get(s)


# Load the survey data from a CSV file
filename = "week3_survey_messy.csv"
SUMMARY_FILE = "week3_summary.txt"
rows = []

with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# Count responses by role
# Normalize role names so "ux researcher" and "UX Researcher" are counted together
role_counts = {}

for row in rows:
    # Empty role produced a blank bucket in counts; (x or "") also avoids rare None values.
    role = (row["role"] or "").strip().title()
    if not role:
        role = "Unknown"
    if role in role_counts:
        role_counts[role] += 1
    else:
        role_counts[role] = 1

lines = []
lines.append("Responses by role:")
for role, count in sorted(role_counts.items()):
    line = f"  {role}: {count}"
    lines.append(line)
    print(line)

# Average years of experience: only rows with parseable values (old code crashed on bad cells).
experience_values = []
for row in rows:
    years = parse_experience_years(row["experience_years"])
    if years is not None:
        experience_values.append(years)

avg_experience = sum(experience_values) / len(experience_values)
avg_line = f"\nAverage years of experience: {avg_experience:.1f}"
lines.append(avg_line)
print(avg_line)

# Top 5 highest satisfaction scores (default sort is ascending; we need reverse=True for "top").
scored_rows = []
for row in rows:
    if row["satisfaction_score"].strip():
        scored_rows.append((row["participant_name"], int(row["satisfaction_score"])))

scored_rows.sort(key=lambda x: x[1], reverse=True)
top5 = scored_rows[:5]

lines.append("\nTop 5 satisfaction scores:")
print("\nTop 5 satisfaction scores:")
for name, score in top5:
    line = f"  {name}: {score}"
    lines.append(line)
    print(line)

# Write the same text to a clean summary file for submission / review.
with open(SUMMARY_FILE, "w", encoding="utf-8") as out:
    out.write("\n".join(lines) + "\n")
print(f"\nWrote summary to {SUMMARY_FILE}")
