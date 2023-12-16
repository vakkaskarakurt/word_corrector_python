from damerau_low import damerau_levenshtein
from jaro import jaro_similarity

def combine_distance(word1, word2):
    ratio = length_ratio(word1, word2)
    if ratio > 1.5:
        return 5000
    jaro = jaro_similarity(word1, word2)
    if jaro < 2/3:
        return 5000
    damerau_distance = damerau_levenshtein(word1, word2)
    
    combine_distance = (damerau_distance**2) / jaro

    return combine_distance

def length_ratio(word1, word2):
    dist = abs(len(word1) - len(word2))

    min_length = min(len(word1), len(word2))
    if min_length == 0:
        min_length = 0.0000001
    ratio = dist / min_length

    # ratio = (dist / len(word2)) + 1

    if ratio == 0:
        ratio = 0.0000001
    return ratio + 1

# Example usage:
# print(combine_distance("keti", "kete"))
# print(combine_distance("keti", "kedi"))
# print(combine_distance("keti", "ket"))
