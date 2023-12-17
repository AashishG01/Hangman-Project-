#Step 1 
import Hangman_words
import Hangman_art
import random

hangman_logo = Hangman_art.logo
print(hangman_logo)
word_list = Hangman_words.words_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

n = random.randint(0,2)
chosen_word = word_list[n]
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess the letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in range(0,len(chosen_word)):
  if guess == chosen_word[i]:
    print("Right")
  else:
    print("Wrong")
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for i in range(0,len(chosen_word)):
  display.append("_")
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for i in range(0,len(chosen_word)):
  if guess == chosen_word[i]:
    display[i] = guess
print(display)
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
hangman_stages = Hangman_art.stages
num = 6
lives = int(num)
#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."
while(display.count("_")>0 and lives>0):
  guess = input("Guess the letter: ").lower()
  x = display.count('_')

  for i in range(0,len(chosen_word)):
    if guess == chosen_word[i]:
      print("Right")
    else:
      print("Wrong")
  for i in range(0,len(chosen_word)):
    if guess == chosen_word[i]:
      display[i] = guess

  c = display.count('_')

  if c == x :
    lives = lives - 1
    print(hangman_stages[lives])
    print(f"You have {lives} lives left")
  
  print(display)

if lives == 0:
  print("You lose")
else:
  print("You win")
