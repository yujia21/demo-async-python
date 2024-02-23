import time


def run_task(i: int) -> None:
    print(f"task {i} sleeping")
    time.sleep(1)
    print(f"task {i} woke up")


def run_all() -> None:
    start = time.time()
    for i in range(5):
        run_task(i)
    print(f"total time taken: {time.time() - start}")


if __name__ == "__main__":
    run_all()
