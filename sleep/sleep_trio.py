import time

import trio


async def run_task(i: int) -> None:
    print(f"task {i} sleeping")
    await trio.sleep(1)
    print(f"task {i} woke up")


async def run_all() -> None:
    start = time.time()
    async with trio.open_nursery() as nursery:
        for i in range(5):
            nursery.start_soon(run_task, i)
    print(f"total time taken: {time.time() - start}")


if __name__ == "__main__":
    trio.run(run_all)
