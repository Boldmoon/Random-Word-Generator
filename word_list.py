def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = word_file.read().split()
    return valid_words


word_list = load_words()
print(word_list)
