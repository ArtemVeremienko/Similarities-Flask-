from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    lines_a = set(a.split('\n'))
    lines_b = set(b.split('\n'))
    return lines_a & lines_b


def sentences(a, b):
    """Return sentences in both a and b"""
    sent_a = set(sent_tokenize(a))
    sent_b = set(sent_tokenize(b))
    return sent_a & sent_b


def substrings_tokenize(str, n):
    """Return list of substrings"""
    substring = []
    for i in range(len(str) - n + 1):
        substring.append(str[i:i + n])
    return substring

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    substring_a = set(substrings_tokenize(a, n))
    substring_b = set(substrings_tokenize(b, n))
    return substring_a & substring_b
