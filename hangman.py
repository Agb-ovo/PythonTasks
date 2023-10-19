import random
import string
from words import words





def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
       
    return word

def hangman():
    word = get_valid_word(words)
    print(f"Your word is {word}")
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
     # Initialize an empty list to store the characters
 
     #getting user input
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have used these letters:', ' '.join(used_letters))

        # what current word is (ie W - R D)

        word_list = [letter if letter.upper() in used_letters else '-' for letter in word]    
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()


        #word_list = []
        #for letter in word:
            #print(f"letter: {letter}")
            #if letter == user_letter.lower():                
                #word_list.append(letter)  # If the letter is in used_letters, add it to word_list
            #elif user_letter != used_letters:
                #word_list.append('-')  # If the letter is not in used_letters, add '-' to word_list

        
        #print(word_list)
        #print(word_letters)

        
        if user_letter in alphabet and user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else: 
                lives = lives - 1
                print('You have already used that character. Please try again')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again')

     #gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)  
    else:
        print('You guessed the word', word,  '!!')     

    

hangman()



