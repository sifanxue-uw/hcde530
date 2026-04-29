import csv
import json
import sys
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ENDPOINT = "https://hcde530-week4-api.onrender.com/reviews"


def fetch_json(url: str):
    req = Request(url, headers={"Accept": "application/json", "User-Agent": "hcde530-week4-script/1.0"})
    with urlopen(req, timeout=30) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        body = resp.read().decode(charset)
    return json.loads(body)


def extract_reviews(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("reviews", "data", "results", "items"):
            if isinstance(payload.get(key), list):
                return payload[key]
    raise ValueError("Unexpected API response shape (expected a list, or a dict containing a list).")


def main():
    try:
        payload = fetch_json(ENDPOINT)
        reviews = extract_reviews(payload)
    except (HTTPError, URLError, TimeoutError) as e:
        print(f"Error fetching {ENDPOINT}: {e}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {ENDPOINT}: {e}", file=sys.stderr)
        return 1

    # 2) Print the requested fields
    for idx, r in enumerate(reviews, start=1):
        category = r.get("category")
        helpful_votes = r.get("helpful_votes")
        print(f"{idx}. category={category!r} helpful_votes={helpful_votes!r}")

    # 3) Save to CSV (write whatever keys appear across items)
    all_keys = set()
    for r in reviews:
        if isinstance(r, dict):
            all_keys.update(r.keys())
    fieldnames = sorted(all_keys)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = f"reviews_{timestamp}.csv"

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for r in reviews:
            writer.writerow(r if isinstance(r, dict) else {"value": r})

    print(f"\nWrote {len(reviews)} rows to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

