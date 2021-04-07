import time


class Timer:
    def __init__(self, title=None):
        self.title = title
        self._start = None

    def __enter__(self):
        print("Count has started")
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        duration = end - self._start
        print(f"Block {self.title} was executed in {round(duration, 4)} sec")


if __name__ == '__main__':
    with Timer("peace of code") as timer:
        for number in range(10):
            time.sleep(1)
