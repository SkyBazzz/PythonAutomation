import re
from socket import inet_aton


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


if __name__ == '__main__':
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
