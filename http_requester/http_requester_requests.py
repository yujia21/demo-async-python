import time

import requests


def get_data(data_type: str) -> None:
    print(f"Fetching {data_type}")
    with requests.Session() as session:
        res = session.get(f"https://api.data.gov.sg/v1/environment/{data_type}")
        print(f"{data_type} response: {res.json()}\n")


def main() -> None:
    start = time.time()
    data_types = [
        "air-temperature",
        "rainfall",
        "relative-humidity",
        "pm25",
        "psi",
        "uv-index",
    ]
    for data_type in data_types:
        get_data(data_type)
    print(f"total time taken: {time.time() - start}")


main()
