import csv
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


# Seattle Open Data (Socrata) dataset: Fremont Bridge hourly bicycle counts.
# This URL is the "resource" endpoint for one table; appending query params (e.g. $limit)
# filters how many rows the server returns. No API key is required for this public dataset.
API_ENDPOINT = "https://data.seattle.gov/resource/65db-xm6k.json"


def fetch_records(limit: int = 1000):
    # $limit caps how many records we download in one request (Socrata supports paging too).
    url = f"{API_ENDPOINT}?{urlencode({'$limit': limit})}"

    # Tell the server we want JSON and identify the client (some servers block blank user agents).
    req = Request(url, headers={"Accept": "application/json", "User-Agent": "hcde530-week4-script/1.0"})

    # The API returns an HTTP response whose body is JSON text (UTF-8 by default).
    with urlopen(req, timeout=30) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        body = resp.read().decode(charset)

    # After json.loads, we expect a Python list where each item is one hour's record (a dict).
    data = json.loads(body)
    if not isinstance(data, list):
        raise ValueError("Unexpected response shape: expected a list of records.")
    return data


def main():
    try:
        # 1) Call the API: network request + JSON parse into a list of dicts.
        records = fetch_records(limit=1000)
    except (HTTPError, URLError, TimeoutError) as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}", file=sys.stderr)
        return 1

    # 2) Extract three fields per record for structured output we can analyze or share.
    # - date: when the count was taken (time series / trends, seasonality).
    # - fremont_bridge_nb / fremont_bridge_sb: northbound vs southbound volumes (directional demand).
    # Together they describe real travel patterns on a major bike corridor (useful for HCD and planning).
    rows = []
    for r in records:
        rows.append(
            {
                "date": r.get("date"),
                "fremont_bridge_nb": r.get("fremont_bridge_nb"),
                "fremont_bridge_sb": r.get("fremont_bridge_sb"),
            }
        )

    # 3) Human-readable check: print each slimmed-down record so you can spot bad or missing values.
    for row in rows:
        print(row)

    # 4) Persist the same structured rows as CSV for spreadsheets, charts, or later Python analysis.
    out_path = "seattle_bikes.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "fremont_bridge_nb", "fremont_bridge_sb"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nWrote {len(rows)} rows to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

