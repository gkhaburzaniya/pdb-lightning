def count_words(text, word):
    """ Counts the number of occurances of the word in text. """
    word_count = 0
    for text_word in text.split():
        if text_word == word:
            word_count += 1
    return word_count
