import asyncio
import time

import aiohttp


async def get_data(data_type: str) -> None:
    print(f"Fetching {data_type}")
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://api.data.gov.sg/v1/environment/{data_type}"
        ) as response:
            res = await response.json()
            print(f"{data_type} response: {res}\n")


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
    await asyncio.gather(*[get_data(data_type) for data_type in data_types])
    print(f"total time taken: {time.time() - start}")


asyncio.run(main())
