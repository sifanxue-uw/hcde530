#!/usr/bin/env python3

import argparse
import csv
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


BASE_URL = "https://hcde530-week4-api.onrender.com"


def fetch_json(url: str, timeout_s: int = 30) -> dict:
    req = Request(url, headers={"Accept": "application/json"})
    try:
        with urlopen(req, timeout=timeout_s) as resp:
            charset = resp.headers.get_content_charset() or "utf-8"
            return json.loads(resp.read().decode(charset))
    except (HTTPError, URLError) as e:
        raise RuntimeError(f"Request failed for {url}: {e}") from e


def iter_reviews(limit: int = 100):
    offset = 0
    while True:
        qs = urlencode({"limit": limit, "offset": offset})
        payload = fetch_json(f"{BASE_URL}/reviews?{qs}")
        reviews = payload.get("reviews", [])
        if not reviews:
            return
        for r in reviews:
            yield r
        offset += len(reviews)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Fetch review category + helpful votes from the HCDE 530 Week 4 API and save to CSV."
    )
    parser.add_argument(
        "--out",
        default="api_category_helpful_votes.csv",
        help="Output CSV filename (default: %(default)s)",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=100,
        help="How many reviews to request per page (default: %(default)s)",
    )
    args = parser.parse_args(argv)

    rows = []
    for review in iter_reviews(limit=args.page_size):
        category = review.get("category")
        helpful_votes = review.get("helpful_votes")
        print(f"{category}\t{helpful_votes}")
        rows.append({"category": category, "helpful_votes": helpful_votes})

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["category", "helpful_votes"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nWrote {len(rows)} rows to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
