from textdistance import jaro
from textdistance import jaro_winkler


def jaro_similarity(kelime1, kelime2):
    jaro_sim = jaro_winkler(kelime1, kelime2)
    if jaro_sim == 0:
        jaro_sim = 0.0000001
    return jaro_sim
