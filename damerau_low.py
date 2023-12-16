import numpy as np
from letter_distance import letter_distance
import textdistance


def damerau_levenshtein(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    d = [[0 for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]

    for i in range(len_s1 + 1):
        d[i][0] = i

    for j in range(len_s2 + 1):
        d[0][j] = j

    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            cost = 0 if s1[i - 1] == s2[j -
                                        1] else (letter_distance(s1[i - 1], s2[j - 1]) / 2 + 0.5)
            d[i][j] = min(
                d[i - 1][j] + 1,         # deletion
                d[i][j - 1] + 1,         # insertion
                d[i - 1][j - 1] + cost   # substitution (using letter distance)
            )

            if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + cost)  # transposition

    return d[len_s1][len_s2]


def damerau_low2(kelime1, kelime2):
    distance = textdistance.damerau_levenshtein(kelime1, kelime2)
    return distance

# Test the function
# print(damerau_levenshtein("vakkas", "asffasfas"))
