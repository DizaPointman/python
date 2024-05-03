def square(number):
    if 0 < number <= 64:
            if number == 1:
                return number
            else:
                return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    return sum([1] + [2 ** num for num in range(1, 64)])
