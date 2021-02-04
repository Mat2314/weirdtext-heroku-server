"""
File contains proper set of functions enabling decoding the weirdtext to the original form.
"""
import re


def check_input_validity(weirdtext: str, original_words: list):
    """
    Function checks if weirdtext is passed in proper form for our encoder and decoder.
    If not then the exception is raised.
    :param weirdtext: Encoded text
    :param original_words: list of original words from the text before it was encoded
    :return:
    """
    # First check magic separator in the text
    magic_separator = "\n--weird--\n"
    if not weirdtext.startswith(magic_separator) or not weirdtext.endswith(magic_separator):
        raise ValueError("Weirdtext does not contain a magic separator")

    # Now remove the magic separator
    weirdtext_edited = weirdtext.replace(magic_separator, "")

    # Extract all the words
    tokenize_re = re.compile(r'(\w+)', re.U)
    list_of_words = tokenize_re.findall(weirdtext_edited)

    # Check if the amount of words is exactly the same as in original version
    if len(original_words) != len(list_of_words):
        raise ValueError('Words length in both versions differ')

    # Check a couple of first words
    list_of_words.sort()
    if len(list_of_words) > 5:
        words_to_check = 5
    else:
        words_to_check = len(list_of_words)

    for i in range(words_to_check):
        if len(list_of_words[i]) != len(original_words[i]):
            raise ValueError('One of the first words length differ')


def decode_word(encoded_word: str, original_words: list) -> str:
    """
    Function is iterating through original_words and looks for matching word to the encoded word.
    When it finds one it returns its value.
    :param encoded_word: The encoded word
    :param original_words: List of original words returned by encoder
    :return: Decoded word found in original_words list
    """
    for word in original_words:
        if len(word) == len(encoded_word) and word[0] == encoded_word[0] and word[-1] == encoded_word[-1]:
            # If both words are the same size and their edge letters are the same return the word as decoded
            return word


def decode(weirdtext: str, original_words: list) -> str:
    """
    Function is processing weirdtext and decoding it to the original plaintext.
    :param weirdtext: Encoded text
    :param original_words: list of original words from the text before it was encoded
    :return: original_message: string
    """
    # First check if weirdtext looks like text encoded with our encoder
    # If not raise exception ValueError
    try:
        check_input_validity(weirdtext, original_words)
    except ValueError as e:
        raise ValueError('Function can not be executed due to incorrect input value: ', e.args[0])

    # Clean weirdtext from separators
    magic_separator = "\n--weird--\n"
    weirdtext = weirdtext.replace(magic_separator, "")

    # Extract all the words
    tokenize_re = re.compile(r'(\w+)', re.U)
    encoded_words = tokenize_re.findall(weirdtext)

    # Decode all the words
    decoded_words_list = [decode_word(word, original_words) for word in encoded_words]

    # Substitute encoded words with decoded words
    original_message = weirdtext
    for i in range(len(decoded_words_list)):
        original_message = original_message.replace(encoded_words[i], decoded_words_list[i], 1)

    return original_message
