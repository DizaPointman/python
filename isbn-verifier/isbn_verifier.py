def is_valid(isbn):
    print(isbn)
    isbn = [10 if c == 'X' else int(c) for c in isbn if c == 'X' or c.isnumeric()]
    if len(isbn) != 10:
        return False
    else:
        print(f"before reverse: {isbn}")
        isbn = isbn[::-1]
        print(f"after reverse: {isbn}")
        return sum([d * (c + 1) for c, d in enumerate(isbn)]) % 11 == 0