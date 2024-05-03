def is_isogram(string):
    string = [c for c in string.upper() if c.isalpha()]
    return len(string) == len(set(string))
