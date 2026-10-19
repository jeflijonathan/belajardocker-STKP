import multiprocessing
import os
import time


def get_cpu_core():
    with open("/proc/self/stat", "r") as f:
        data = f.read().split()

    # Linux field 39 = processor/core
    return data[38]


def task_a():
    pid = os.getpid()

    for number in [1, 2]:
        core = get_cpu_core()
        result = number ** 2

        print(
            f"[CORE {core}] [PID {pid}] "
            f"TASK A: {number}² = {result}",
            flush=True
        )

        time.sleep(3)


def task_b():
    pid = os.getpid()

    for number in [3, 4]:
        core = get_cpu_core()
        result = number ** 2

        print(
            f"[CORE {core}] [PID {pid}] "
            f"TASK B: {number}² = {result}",
            flush=True
        )

        time.sleep(3)


if __name__ == "__main__":

    print("=" * 50)
    print("      SIMULASI 1 CPU CORE - 2 TASK")
    print("=" * 50)

    process_a = multiprocessing.Process(target=task_a)
    process_b = multiprocessing.Process(target=task_b)

    process_a.start()
    process_b.start()

    process_a.join()
    process_b.join()

    print("\n=== SEMUA TASK SELESAI ===")
    print("Task A = 1² + 2²", )
    print("Task B = 3² + 4² = 25")
    print("Total   = 30")