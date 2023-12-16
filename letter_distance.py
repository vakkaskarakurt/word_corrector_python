keyboard = {
    'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'ı': (0, 7), 'o': (0, 8), 'p': (0, 9), 'ğ': (0, 10), 'ü': (0, 10),
    'a': (1, 0.3), 's': (1, 1.3), 'd': (1, 2.3), 'f': (1, 3.3), 'g': (1, 4.3), 'h': (1, 5.3), 'j': (1, 6.3), 'k': (1, 7.3), 'l': (1, 8.3), 'ş': (1, 9.3), 'i': (1, 10.3), ',': (1, 11.3),
    '<': (2, -0.3), 'z': (2, 0.7), 'x': (2, 1.7), 'c': (2, 2.7), 'v': (2, 3.7), 'b': (2, 4.7), 'n': (2, 5.7), 'm': (2, 6.7), 'ö': (2, 7.7), 'ç': (2, 8.7), '.': (2, 9.7),
    'â': (1, 0.3)
}

letter_distance_cache = {}

def letter_distance(letter1, letter2):
    # Return from the cache if a previously calculated result exists
    cached_result = letter_distance_cache.get((letter1, letter2))
    if cached_result is not None:
        return cached_result

    x1, y1 = keyboard.get(letter1, (0, 0))
    x2, y2 = keyboard.get(letter2, (0, 0))

    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    result = distance / 11.34

    # Save the result in the cache
    letter_distance_cache[(letter1, letter2)] = result

    return result
