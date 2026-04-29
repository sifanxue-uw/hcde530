#!/usr/bin/env python3

import csv
import json
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


# This Socrata endpoint returns a JSON list (array) of bike-count records.
# Each record corresponds to an hour and includes counts for the Fremont Bridge
# in the northbound (NB) and southbound (SB) directions.
API_URL = "https://data.seattle.gov/resource/65db-xm6k.json"


def fetch_records(limit: int = 50) -> list[dict]:
    """Fetch records from the Socrata API (JSON list)."""
    # Build a query string.
    # Parameters used:
    # - $limit: how many records to return (we use 50 to satisfy "at least 50 records").
    # - $order: sort by date so we get the most recent records first.
    qs = urlencode({"$limit": limit, "$order": "date DESC"})
    url = f"{API_URL}?{qs}"

    # Create an HTTP request that asks for JSON
    req = Request(url, headers={"Accept": "application/json"})

    try:
        # Make the network call and decode the JSON response
        with urlopen(req, timeout=30) as resp:
            charset = resp.headers.get_content_charset() or "utf-8"
            return json.loads(resp.read().decode(charset))
    except (HTTPError, URLError) as e:
        # Turn urllib errors into a clear, single exception for the user
        raise RuntimeError(f"Request failed for {url}: {e}") from e


def main() -> int:
    # Always write the CSV next to this script, regardless of the terminal's current directory
    out_path = Path(__file__).resolve().parent / "seattle_bikes.csv"

    # Call the API endpoint (step 1) and get a list of records back.
    records = fetch_records(limit=50)

    all_rows: list[dict] = []
    for r in records:
        # Extract the three requested fields from each record (step 2)
        # Field meanings:
        # - date: the hour timestamp for the count (ISO datetime string)
        # - fremont_bridge_nb: number of people/bikes counted northbound during that hour
        # - fremont_bridge_sb: number of people/bikes counted southbound during that hour
        row = {
            "date": r.get("date"),
            "fremont_bridge_nb": r.get("fremont_bridge_nb"),
            "fremont_bridge_sb": r.get("fremont_bridge_sb"),
        }

        # Print each record (step 3)
        print(row)

        # Store the row so we can write everything to CSV (step 4)
        all_rows.append(row)

    # Write the collected rows to a CSV file (step 4)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "fremont_bridge_nb", "fremont_bridge_sb"])
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"\nWrote {len(all_rows)} rows to {out_path}")
    return 0


if __name__ == "__main__":
    # Run the script and return a proper exit code to the shell
    raise SystemExit(main())
