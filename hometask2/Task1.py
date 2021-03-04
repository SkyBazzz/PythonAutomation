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


if __name__ == '__main__':
    elements = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
    print(for_filtering(elements))
    print(list_comprehension_filtering(elements))
    print(lambda_filtering(elements))
