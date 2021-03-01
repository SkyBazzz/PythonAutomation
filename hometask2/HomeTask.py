import re
import os
import sys
import argparse
from csv import DictReader
from socket import inet_aton
from json import dump


# Task #1. Filter list.
def for_filtering(collection: list):
    values = list()
    for i in collection:
        if isinstance(i, int):
            values.append(i)

    return values


def list_comprehension_filtering(collection: list):
    return [i for i in collection if isinstance(i, int)]


def lambda_filtering(collection: list):
    int_ = is_int()
    return list(filter(int_, collection))


def is_int():
    return lambda x: isinstance(x, int)


# Task #2. Validate IP.
def is_valid_ip(ip_address) -> bool:
    try:
        inet_aton(ip_address)
        return True
    except OSError:
        return False
    except TypeError:
        return False


def is_valid_ip_re(ip_address) -> bool:
    pat = re.compile(r"^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){3,4}$")
    test = pat.match(str(ip_address))
    if test:
        return True
    else:
        return False


# Task #3. Work with csv and json structures.
def read_file(file_name: str):
    json_data = create_data_from_csv(file_name)
    write_to_json(json_data)


def create_data_from_csv(file_name):
    json_data = list()
    with open(file_name, encoding='utf-8') as csv_file:
        csv_cars = DictReader(csv_file)
        for csv_row in csv_cars:
            json_data.append(csv_row)
    return json_data


def write_to_json(data):
    with open('cars.json', mode='w', encoding='utf-8') as cars_json:
        dump(data, cars_json, indent=2)


# Task #4. Unix Find
def find(folder, name=None, show_dirs=True, show_files=True):
    """
       :param folder: path to a system folder from where to start searching
       :param name: file/directory name pattern, allows using '*' and '?' symbols
       :param show_dirs: if True - include directories into search results
       :param show_files: if True - include files into search results
       """
    for root, dirs, files in os.walk(folder):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))


def parse_cmd_args():
    path_help = "Path to a folder"
    name_help = "File name pattern. Allows using '*' and '?' symbols"
    type_help = "Where 'f' means search only files, 'd' means only directories"

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help=path_help)
    parser.add_argument('-name', nargs='?', default=None, help=name_help)
    parser.add_argument('-type', nargs='?', default=None, choices=['f', 'd'], help=type_help)

    if len(sys.argv) <= 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    cmd, _ = parser.parse_known_args()

    files, dirs = True, True
    if cmd.type == 'd':
        files = False
    if cmd.type == 'f':
        dirs = False
    return cmd.path, cmd.name, dirs, files


if __name__ == '__main__':
    elements = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
    print(for_filtering(elements))
    print(list_comprehension_filtering(elements))
    print(lambda_filtering(elements))
    print("=" * 20)
    assert is_valid_ip('') is False
    assert is_valid_ip('192.168.0.1') is True
    assert is_valid_ip('0.0.0.1') is True
    assert is_valid_ip('10.100.500.32') is False
    assert is_valid_ip(700) is False
    assert is_valid_ip('127.0.1') is True

    assert is_valid_ip_re('') is False
    assert is_valid_ip_re('192.168.0.1') is True
    assert is_valid_ip_re('0.0.0.1') is True
    assert is_valid_ip_re('10.100.500.32') is False
    assert is_valid_ip_re(700) is False
    assert is_valid_ip_re('127.0.1') is True

    read_file('cars.csv')
    find(r'C:\Users\Oleksandr_Balkashyn\PycharmProjects')