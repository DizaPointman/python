def is_pangram(sentence):
    sentence = set([c for c in sentence.upper() if c.isalpha()])
    return len(sentence) == 26
