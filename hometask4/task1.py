import re


def my_function(text, multiplier=2):
    return re.sub('\d+', lambda number: str(int(number.group(0)) * multiplier), text)


if __name__ == '__main__':
    print(my_function(
        '''Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира, только у троих футболистов средний
показатель превышает 2 гола за игру. Эти 35 игроков представляют 14 футбольных сборных''', 3))
    print(my_function('I am 25 years old'))
    print(my_function('I am 25 years old', 10))
