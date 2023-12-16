from textdistance import jaro
from textdistance import jaro_winkler


def jaro_similarity(word1, word2):
    jaro_sim = jaro_winkler(word1, word2)
    if jaro_sim == 0:
        jaro_sim = 0.0000001
    return jaro_sim
