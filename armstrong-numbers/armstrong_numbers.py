def is_armstrong_number(number):
    nums = [c for c in str(number)]
    return number == sum([((int(num)) ** len(nums)) for num in nums])