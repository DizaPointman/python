def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if type(number) != int or number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        result = [n for n in range(1, number) if number % n == 0]
        if sum(result) == number: return "perfect"
        if sum(result) > number: return "abundant"
        if sum(result) < number: return "deficient"
