from gensim.models import KeyedVectors

# Load the pre-trained word vectors model
word_vectors = KeyedVectors.load('model_save')


def vector(word1, word2):
    # Check if either word1 or word2 is empty or None
    if word1 == "" or word1 is None:
        return 0

    if word2 == "" or word2 is None:
        return 0

    try:
        # Calculate the similarity between the two words using word vectors
        return word_vectors.similarity(word1, word2)
    except KeyError:
        # Handle the case where either word1 or word2 is not present in the word vectors
        # Return a default value or take any appropriate action.
        return 0

# Example usage:
# print(vector("kedi", "saldırmak"))
