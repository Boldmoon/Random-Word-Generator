import random

print("Welcome To Random Word Generator")


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = word_file.read().split()
    return valid_words


word_list = load_words()
random.shuffle(word_list)
count_loop_con = True
letter_loop_con = True
word_count_loop_con = True
awf = False
random_words = []

while count_loop_con:
    letter_count = input("How many letters should the words have? ")
    if letter_count.isdigit():
        letter_count = int(letter_count)
        count_loop_con = False
    else:
        print("Please enter the proper number of letters that the words must have.")
        print("")

while word_count_loop_con:
    word_count = input("How many random words should be made? ")
    if word_count.isdigit():
        word_count = int(word_count)
        word_count_loop_con = False
    else:
        print("Please enter a proper number of random words to generate.")
        print("")

while letter_loop_con:
    start_letter = input("What should be the starting letter for the words? ")
    end_letter = input("What should be the ending letter for the words? ")
    if start_letter.isalpha() and end_letter.isalpha() and len(start_letter) == 1 and len(end_letter) == 1:
        letter_loop_con = False
    else:
        print("Please enter proper start and end letters.")
        print("")

for word in word_list:
    if len(word) == letter_count and word[0] == start_letter and word[letter_count - 1] == end_letter:
        if len(random_words) == word_count:
            awf = True
            break
        else:
            random_words.append(word)

if awf:
    print(f"{word_count} random words generated with {letter_count} letters with starting letter as {start_letter}, "
          f"ending letter as {end_letter}.")
    print(*random_words)
elif len(random_words) == 0:
    print(
        f"No {word_count} random words were generated with {letter_count} letters with starting letter as {start_letter} ending letter as {end_letter}.")
else:
    print("Only the below words were available for the inputted conditions: ")
    print(*random_words)

print("\nThank You")
print("An application developed by Harish Ashok")
print("Habril Inc. :)")
