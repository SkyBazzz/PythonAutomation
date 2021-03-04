import os
import prettytable
import argparse
import sys


# Task #5. Unix ls -lh for windows without group and user
def ls_lh(path):
    listdir = os.listdir(path)
    table = prettytable.PrettyTable()
    table.field_names = ["Mode", "Size", "File Name"]

    for file in listdir:
        table.add_row([os.stat(file).st_mode, os.stat(file).st_size, file])
    table.align["Size"] = 'r'
    print(table.get_string(title="File Info", sortby="Size", reversesort=True))


def parse_cmd_args():
    path_help = "Path to a folder"

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help=path_help)

    if len(sys.argv) < 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    cmd, _ = parser.parse_known_args()
    return cmd.path


if __name__ == '__main__':
    file_path = parse_cmd_args()
    ls_lh(file_path)
