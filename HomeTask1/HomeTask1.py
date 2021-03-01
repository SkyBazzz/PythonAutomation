import sys
from string import ascii_lowercase


# Task #1. Fizz Buzz
# def fizz_buzz():
#     for number in range(1, 100):
#         if number % 3 == 0 and number % 5 != 0:
#             print("Fizz")
#         elif number % 3 != 0 and number % 5 == 0:
#             print("Buzz")
#         elif number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         else:
#             print(number)


# Task #2. Find min and max
def min_and_max():
    numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
    min_value = numbers[0]
    max_value = numbers[0]
    for number in numbers:
        try:
            value = int(number)
            if value > max_value:
                max_value = value
            if value < min_value:
                min_value = value
            print(int(number))
        except TypeError:
            pass
        except ValueError:
            pass
    print(f"Min value is = {min_value}")
    print(f"Max value is = {max_value}")


# Task #3. Letters count. Python count.
def letters_count():
    dictionary = {}
    accuracy = 0
    with open('story', 'r', encoding='UTF8') as story:
        for line in story:
            formatted_line = line.lower()
            accuracy += formatted_line.count('python')
            count_letters(dictionary, formatted_line)

    print(f"Word Python (ignore case) was presented {accuracy} time(s).")
    most_freq_letter = max(dictionary, key=dictionary.get)
    print(f"Most frequently used letter is {most_freq_letter} - {dictionary[most_freq_letter]} time(s).")


def count_letters(dictionary, line):
    for letter in ascii_lowercase:
        if letter not in dictionary:
            dictionary[letter] = line.count(letter)
        else:
            dictionary[letter] += line.count(letter)


# Task #4. Find sum of multipliers 3 and 5
def multiples_3_5_sum(n):
    threes = 3 * (n // 3 + 1) * (n // 3) / 2
    fives = 5 * (n // 5 + 1) * (n // 5) / 2
    fifteens = 15 * (n // 15 + 1) * (n // 15) / 2

    result = threes + fives - fifteens
    return int(result)


def loops(number):
    result = 0
    for value in range(3, number + 1, 3):
        result += value
    for value in range(5, number + 1, 5):
        result += value
    for value in range(15, number + 1, 15):
        result -= value
    return result


# Task #5. Get file size from bytes.
def file_size(size):
    power = 2 ** 10
    counter = 0
    label = 'B'
    while size > power:
        if counter == 3:
            break
        size /= power
        counter += 1
    if counter == 1:
        label = "Kb"
    elif counter == 2:
        label = "Mb"
    elif counter >= 3:
        label = "Gb"

    return f"{float(size):.1f}{label}"


def line_separator():
    print("=" * 25)


if __name__ == '__main__':
    # fizz_buzz()
    line_separator()
    min_and_max()
    line_separator()
    letters_count()
    line_separator()
    i = 10000000
    print(f"Result {multiples_3_5_sum(i)}")
    line_separator()
    print(f"Result {loops(i)}")
    line_separator()
    assert file_size(19) == '19.0B'
    assert file_size(12345) == '12.1Kb'
    assert file_size(1101947) == '1.1Mb'
    assert file_size(572090) == '558.7Kb'
    assert file_size(999999999999) == '931.3Gb'
    print(file_size(19))
    print(file_size(12345))
    print(file_size(1101947))
    print(file_size(572090))
    print(file_size(9223372036854776000))
    line_separator()
    print(file_size(sys.maxsize))
