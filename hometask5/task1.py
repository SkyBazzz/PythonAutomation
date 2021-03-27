import threading
import requests
import json
import traceback
import time


def time_it(func):
    def timed(path):
        ts = time.time()
        result = func(path)
        te = time.time()
        print((te - ts))
        return result
    return timed


@time_it
def verify_links(file_path):
    objs = list()
    with open(file_path, "r") as links:
        threads = list()
        for link in links:
            x = threading.Thread(target=verify_link, args=(link, objs))
            threads.append(x)
            x.start()
        for index, thread in enumerate(threads):
            print(index, thread.name)
            thread.join()
    write_result(objs)


def verify_link(link, objs):
    f_link = link.strip("\n")
    try:
        response = requests.get(f_link)
        if response.ok:
            obj = {"url": response.url, "is_ok": True, "status_code": response.status_code}
        else:
            obj = {"url": response.url, "is_ok": False, "status_code": response.status_code}
    except Exception:
        traceback.print_exc()
        obj = {"url": f_link, "is_ok": False, "status_code": None}
    print(f"{f_link} verified")
    objs.append(obj)


def write_result(objs):
    with open("links.json", "w") as results:
        json.dump(objs, results, indent=2)


if __name__ == '__main__':
    verify_links("links.txt")
