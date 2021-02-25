import re
from socket import inet_aton


# Task #1. Filter list
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


# Task #2. Validate IP
def is_valid_ip(ip_address) -> bool:
    try:
        inet_aton(ip_address)
        return True
    except OSError as e:
        return False
    except TypeError as e:
        return False


def is_valid_ip_re(ip_address) -> bool:
    pat = re.compile(r"^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){3,4}$")
    test = pat.match(str(ip_address))
    if test:
        return True
    else:
        return False


if __name__ == '__main__':
    elements = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
    print(for_filtering(elements))
    print(list_comprehension_filtering(elements))
    print(lambda_filtering(elements))
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
