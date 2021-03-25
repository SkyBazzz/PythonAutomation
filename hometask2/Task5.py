import os
import prettytable
import argparse

import win32security


# Task #5. Unix ls -lh for windows without group and user
def ls_lh(path):
    listdir = os.listdir(path)
    table = prettytable.PrettyTable()
    table.field_names = ["Mode", "Size", "User owner", "Group", "File name"]

    for file in listdir:
        file = os.path.join(path, file)
        domain, name = file_owner(file)
        stat = os.stat(file)
        table.add_row([oct(stat.st_mode), stat.st_size, f'{domain}/{name}', stat.st_gid, file])
    table.align["Size"] = 'r'
    print(table.get_string(title="File Info", sortby="Size", reversesort=True))


def file_owner(file):
    sd = win32security.GetFileSecurity(file, win32security.OWNER_SECURITY_INFORMATION)
    owner_sid = sd.GetSecurityDescriptorOwner()
    name, domain, _ = win32security.LookupAccountSid(None, owner_sid)
    return domain, name


def parse_cmd_args():
    path_help = "Path to a folder"
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help=path_help)

    cmd = parser.parse_args()
    return cmd.path


if __name__ == '__main__':
    ls_lh(parse_cmd_args())
