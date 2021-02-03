"""
File contains proper set of functions enabling encoding string to the weirdtext.
"""
import random
import re


def shuffle_word(word: str) -> str:
    """
    Function is encoding given word with the following conditions:
    - first and last character of a word stays the same
    - characters in between are being shuffled
    - final word must not be the same as the original word (if possible)
    :param word: a word that needs to be shuffled
    :return: shuffled_word: string
    """
    if len(word) < 4:
        # Word with 3 letters can not be shuffled with to given conditions
        return word

    # Convert letters to shuffle to list
    letters_to_shuffle = list(word[1:-1])
    sorted_letters = letters_to_shuffle.copy()
    sorted_letters.sort()

    # If all the letters are the same permutation is not possible
    if sorted_letters[0] == sorted_letters[-1]:
        return word

    # Shuffle the letters
    shuffled_letters = letters_to_shuffle.copy()

    while shuffled_letters == letters_to_shuffle:
        random.shuffle(shuffled_letters)

    # List to string
    shuffled_letters = "".join(shuffled_letters)

    # Create a shuffled word and return it
    shuffled_word = word[0] + shuffled_letters + word[-1]
    return shuffled_word


def encode(plaintext: str) -> (str, list):
    """
    Function is encoding given plaintext to a weirdtext form.
    :param plaintext: The string to be encoded
    :return: tuple(encoded_text: string, original_words: list)
    """
    # Compile regular expression into pattern
    # And use it to find all words in the plaintext
    tokenize_re = re.compile(r'(\w+)', re.U)
    original_words = tokenize_re.findall(plaintext)

    # Encode each original word with shuffle_word function
    encoded_words = list(map(shuffle_word, original_words))

    # Substitute original words with encoded words in the plaintext
    for i in range(len(encoded_words)):
        plaintext = plaintext.replace(original_words[i], encoded_words[i], 1)

    # Sort the original words list
    # And add magic value as a separator
    original_words.sort()
    encoded_text = "\n--weird--\n" + plaintext + "\n--weird--\n"

    return encoded_text, original_words
