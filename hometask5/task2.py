"""
These are different solutions of "Task 5: Multiples of 3 and 5. Find the best algorithm"

Let's find out which of the proposed algorithms is the most effective
"""

from multiprocessing import Process
from functools import wraps
import time


def time_it(func):
    @wraps(func)
    def timed():
        ts = time.time()
        result = func()
        te = time.time()
        print(f"{func.__name__} -> {te - ts}")
        return result

    return timed


N = 300000000


@time_it
def simple_iteration():
    res = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


@time_it
def several_for_loops():
    res = 0
    for i in range(3, N, 3):
        res += i
    for i in range(5, N, 5):
        res += i
    for i in range(15, N, 15):
        res -= i
    return res


@time_it
def iterate_over_fifteen():
    range_diff = [0, 3, 5, 6, 9, 10, 12]
    res = 0
    for i in range(0, N, 15):
        for d in range_diff:
            v = i + d
            if v >= N:
                break
            res += v
    return res


@time_it
def math_formula():
    upper = N - 1
    threes = int(3 * (upper / 3) * ((upper / 3) + 1) / 2)
    fives = int(5 * (upper / 5) * ((upper / 5) + 1) / 2)
    fifteens = int(15 * (upper / 15) * ((upper / 15) + 1) / 2)
    res = threes + fives - fifteens
    return res


@time_it
def run_all_calculations_in_parallel():
    # Use multiprocessing library to run all above functions in parallel
    # Print execution time of each function
    run_in_parallel(simple_iteration, several_for_loops, iterate_over_fifteen, math_formula)


def run_in_parallel(*functions):
    proc = []
    for function in functions:
        process = Process(target=function)
        process.start()
        proc.append(process)
    for process in proc:
        process.join()


if __name__ == '__main__':
    run_all_calculations_in_parallel()
