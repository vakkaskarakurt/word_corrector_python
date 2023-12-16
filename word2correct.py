from word2vec_tr import vector
from file_operations import clear_words
from combine import combine_distance
import numpy as np
import joblib
import os

cache_filename = "wordcorrector_cache.pkl"

# Load the cache file for the wordcorrector function
def load_wordcorrector_cache():
    # If the cache file exists, load it
    if os.path.exists(cache_filename):
        return joblib.load(cache_filename)
    # If the cache file does not exist, return an empty dictionary
    return {}

# Save the cache of the wordcorrector function to the cache file
def save_wordcorrector_cache(cache):
    # Save the cache to the specified file
    joblib.dump(cache, cache_filename)

def wordcorrector(misspelled_word):
    # Load the cache
    cache = load_wordcorrector_cache()
    misspelled_word = misspelled_word.lower()
    # If the misspelled word is in the cache, quickly return the correct word
    if misspelled_word in cache:
        # print("Loading from cache...")
        return cache[misspelled_word]
    else:
        # Calculate the similarity distance of the misspelled word with other words
        distance_array = [combine_distance(misspelled_word, word) for word in clear_words]
        # Sort by similarity distances and select the top two correct words
        sorted_indices = np.argsort(distance_array)[:2]
        correct_words = [clear_words[i] for i in sorted_indices[:2]]
        result_array = correct_words[:2]
        # Save the pair of correct words for the misspelled word to the cache
        cache[misspelled_word] = result_array
        save_wordcorrector_cache(cache)
        return result_array

def get_similar_word(word):
    # If the word is None or already exists, directly return the word
    if word is None or word in clear_words:
        return [word]
    else:
        # If the word does not exist, call the wordcorrector function for the correct version
        return wordcorrector(word)

def get_best_pair(word1_similars, word2_similars, word3_similars):
    # Find the best match among three lists of words
    values = [vector(word1, word2) + vector(word2, word3) for word1 in word1_similars for word2 in word2_similars for word3 in word3_similars]
    triples = [(word1, word2, word3) for word1 in word1_similars for word2 in word2_similars for word3 in word3_similars]
    max_value_index = values.index(max(values))
    
    return triples[max_value_index][1]  # Return the main word from the best triple

def word2correct(before_word, main_word, after_word):
    # If there is no main word, return an empty string
    if main_word is None:      
        return ""
    # If the main word exists and is correct, return the main word
    elif main_word in clear_words:
        return main_word

    # Get similar words for the main word
    main_word_similars = get_similar_word(main_word)
    # Get similar words for the previous and next words
    before_word_similars = get_similar_word(before_word)
    after_word_similars = get_similar_word(after_word)

    # If both the previous and next words are missing, find the best match between the main word and next words and return
    if before_word=="" and after_word=="":
        return main_word_similars[0]

    # If the previous word is missing, find the best match between the main word and next words and return
    if before_word is None:
        return get_best_pair(main_word_similars, after_word_similars, after_word_similars)

    # If the next word is missing, find the best match between the previous and main words and return
    if after_word is None:
        return get_best_pair(before_word_similars, main_word_similars, before_word_similars)

    # If both the previous and next words are in the unique words list, find the best match and return
    if before_word in clear_words and after_word in clear_words:
        return get_best_pair(before_word_similars, main_word_similars, after_word_similars)

    # Find the best match for all cases and return
    return get_best_pair(before_word_similars, main_word_similars, after_word_similars)

# print(wordcorrector("vahiş"))
