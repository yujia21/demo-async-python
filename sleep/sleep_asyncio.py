import asyncio
import time


async def run_task(i: int) -> None:
    print(f"task {i} sleeping")
    await asyncio.sleep(1)
    print(f"task {i} woke up")


async def run_all() -> None:
    start = time.time()
    await asyncio.gather(*[run_task(i) for i in range(5)])
    print(f"total time taken: {time.time() - start}")


if __name__ == "__main__":
    asyncio.run(run_all())
