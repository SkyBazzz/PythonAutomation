import os
import argparse
import fnmatch


# Task #4. Unix find on windows. Example python Task4.py C:\ -name hometask2 -type d
def find(folder, name=None, show_dirs=True, show_files=True):
    """
       :param folder: path to a system folder from where to start searching
       :param name: file/directory name pattern, allows using '*' and '?' symbols
       :param show_dirs: if True - include directories into search results
       :param show_files: if True - include files into search results
       """
    if show_files:
        for root, dirs, files in os.walk(folder):
            find_object(files, name, root)
    if show_dirs:
        for root, dirs, files in os.walk(folder):
            find_object(dirs, name, root)


def find_object(o_path, name, root):
    for file_name in o_path:
        if fnmatch.fnmatch(file_name, name):
            print(os.path.join(root, file_name))


def parse_cmd_args():
    path_help = "Path to a folder"
    name_help = "File name pattern. Allows using '*' and '?' symbols"
    type_help = "Where 'f' means search only files, 'd' means only directories"

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help=path_help)
    parser.add_argument('-name', nargs='?', default='*', help=name_help)
    parser.add_argument('-type', nargs='?', default=None, choices=['f', 'd'], help=type_help)

    cmd = parser.parse_args()

    return cmd.path, cmd.name, cmd.type == 'd', cmd.type == 'f'


if __name__ == '__main__':
    find(*parse_cmd_args())
