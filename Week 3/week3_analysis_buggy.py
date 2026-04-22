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


filename = "week3_survey_messy.csv"
rows = []

with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# Count responses by role
role_counts = {}

for row in rows:
    role = row["role"].strip().title()
    if role in role_counts:
        role_counts[role] += 1
    else:
        role_counts[role] = 1

print("Responses by role:")
for role, count in sorted(role_counts.items()):
    print(f"  {role}: {count}")

experience_values = []
for row in rows:
    years = parse_experience_years(row["experience_years"])
    if years is not None:
        experience_values.append(years)

avg_experience = sum(experience_values) / len(experience_values)
print(f"\nAverage years of experience: {avg_experience:.1f}")

scored_rows = []
for row in rows:
    if row["satisfaction_score"].strip():
        scored_rows.append((row["participant_name"], int(row["satisfaction_score"])))

scored_rows.sort(key=lambda x: x[1])
top5 = scored_rows[:5]

print("\nTop 5 satisfaction scores:")
for name, score in top5:
    print(f"  {name}: {score}")
