import random
import string
from words import words

worded = ["the", "good", "thebad", "and" "the ugly"]

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
       
    return word

def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

     #getting user input
    while len(word_letters) > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have used these letters:', ' '.join(used_letters))

        # what current word is (ie W - R D)
        # word_list = [letter if letter in used_letters else '-' for letter in word]
        word_list = []  # Initialize an empty list to store the characters

        for letter in word:
            if letter in used_letters:
                word_list.append(letter)  # If the letter is in used_letters, add it to word_list
            else:
                word_list.append('-')  # If the letter is not in used_letters, add '-' to word_list

        print('Current word: ', ' '.join(word_list), flush=True)
        print(word_list)
        print(word_letters)

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again')


hangman()


