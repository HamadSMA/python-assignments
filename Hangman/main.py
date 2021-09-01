
import random
from word_list import words
from ascii_art import stages, logo
#Pick a random word from word_list.
chosen_word = random.choice(words)
#Using length of chosen_word repeatedly, thereforing storing it in a variable.
word_len = len(chosen_word)
#Number of lives is synced with the index of each stage in ascii_art so it prints in conjuction with losing health.
lives = 6
game_over = False
display = []

print(f"Welcome to:\n{logo}\n")

#Generat a list of spaces to the length of the chosen word.
for _ in range(word_len):
    display += "_"
#Turn the list into a string
print(f"{''.join(display).upper()}")
#Loop the game until all letters guessed or all health lost.
while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess.upper()}!, try another letter")
#The range fonction will generate a position number for each letter in the word.
#That number will be used as an index to locate the letter in the word.
#The index will also be used to replce the space the corresponding "_" place.
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display).upper()}")
#Penalty when guessing the wrong letter
#Ending the game if one of two conditions met
    if guess not in chosen_word:
        print(f"Oh no, {guess.upper()} is not correct, you lost some health!")
        lives-=1
        if lives == 0:
            print("You lose >:")
            game_over = True
    elif "_" not in display:
        game_over = True
        print("You win! :>")
    print(stages[lives])
