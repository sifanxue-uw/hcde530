import argparse

import citydata
import fetch_reviews


def main():
    parser = argparse.ArgumentParser(description="HCDE 530 Week 4 scripts")
    parser.add_argument(
        "--task",
        choices=["fetch_reviews", "citydata"],
        default="fetch_reviews",
        help="Which task to run",
    )
    args = parser.parse_args()

    if args.task == "fetch_reviews":
        return fetch_reviews.main()
    if args.task == "citydata":
        citydata.main()
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())

