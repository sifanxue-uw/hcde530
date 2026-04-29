import json


def main():
    city_populations = {
        "New York, NY": 8336817,
        "Los Angeles, CA": 3979576,
        "Chicago, IL": 2693976,
        "Houston, TX": 2304580,
        "Phoenix, AZ": 1608139,
    }

    with open("citydata.json", "w", encoding="utf-8") as f:
        json.dump(city_populations, f, ensure_ascii=False, indent=2)

    print("Wrote citydata.json")


if __name__ == "__main__":
    main()

