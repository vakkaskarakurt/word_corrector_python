# Import necessary libraries
import re
from word2correct import word2correct
from file_operations import clear_words

def lowercase_words_to_list(input_text):
    # Remove punctuation, spaces, and numbers
    cleaned_text = re.sub(r'[^a-zA-ZğüşıöçĞÜŞİÖÇ\s]', '', input_text, flags=re.UNICODE)
    
    words = cleaned_text.split()  # Split the input text into words
    lowercase_words = [word.lower() for word in words]  # Convert all words to lowercase and store in a list
    return lowercase_words

def list_correct(word_list):
    corrected_list = []
    for word in word_list:
        if word in clear_words:
            corrected_list.append((word, True))
        else:
            # Get the previous word, if there is a word in the list, otherwise leave it empty
            before_word = corrected_list[-1][0] if corrected_list else ""
            # Get the next word, leave it empty if we are at the end of the list
            after_word = word_list[word_list.index(word) + 1] if word_list.index(word) < len(word_list) - 1 else ""
            # Use the function to correct the word and add the corrected word to the list
            corrected_word = word2correct(before_word, word, after_word)
            corrected_list.append((corrected_word, False))

    # Continue until there are no uncorrected words
    while any(not is_correct for _, is_correct in corrected_list):
        for i, (word, is_correct) in enumerate(corrected_list):
            if not is_correct:
                before_word = corrected_list[i - 1][0] if i > 0 else ""  # Get the previous word, leave it empty if we are at the beginning of the list
                after_word = corrected_list[i + 1][0] if i < len(corrected_list) - 1 else ""  # Get the next word, leave it empty if we are at the end of the list
                corrected_word = word2correct(before_word, word, after_word)  # Use the function to correct the word
                corrected_list[i] = (corrected_word, corrected_word in clear_words)  # Update the correction status

    return [word for word, _ in corrected_list]  # Return only the corrected words

def string_correction(input_text):
    word_list = lowercase_words_to_list(input_text)  # Convert the input text to a list of lowercase words
    corrected_list = list_correct(word_list)  # Correct the list of words
    return corrected_list
