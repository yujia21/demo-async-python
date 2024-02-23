import time

import httpx
import trio


async def get_data(data_type: str) -> None:
    print(f"Fetching {data_type}")
    async with httpx.AsyncClient() as client:
        res = await client.get(f"https://api.data.gov.sg/v1/environment/{data_type}")
        print(f"{data_type} response: {res.json()}\n")


async def main() -> None:
    start = time.time()
    data_types = [
        "air-temperature",
        "rainfall",
        "relative-humidity",
        "pm25",
        "psi",
        "uv-index",
    ]
    async with trio.open_nursery() as nursery:
        for data_type in data_types:
            nursery.start_soon(get_data, data_type)
    print(f"total time taken: {time.time() - start}")


trio.run(main)
