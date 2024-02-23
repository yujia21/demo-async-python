import time

from anyio import create_task_group, run, sleep


async def run_task(i: int) -> None:
    print(f"task {i} sleeping")
    await sleep(1)
    print(f"task {i} woke up")


async def run_all() -> None:
    start = time.time()
    async with create_task_group() as tg:
        for i in range(5):
            tg.start_soon(run_task, i)
    print(f"total time taken: {time.time() - start}")


if __name__ == "__main__":
    run(run_all, backend="trio")
