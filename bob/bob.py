def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob.isupper():
        if hey_bob.endswith('?'):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif not hey_bob.isspace() and len(hey_bob) != 0:
        if hey_bob.endswith('?'):
            return "Sure."
        else:
            return "Whatever."
    else:
        return "Fine. Be that way!"
