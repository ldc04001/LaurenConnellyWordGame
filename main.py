### Setup Section ###

from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]
    secret = actual
    
    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if(letter in secret):   
    
      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == secret[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:

        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)
        
    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
      
    print(Style.RESET_ALL + " ", end="")

# Write a Function that takes in a six-lettered word from the user
def getUserGuess(userWord):
  userGuess = ""

  # if the word is less than or greater than 6 letters, ask the user to guess again
  while(len(userGuess) > 6 or len(userGuess) <6):
    userGuess = input("Enter a six letter word: ")

# store ther user's guess
  return userGuess.lower()
  

# This marks the end of the function definitions, below this is where the program will actually start!

### Main Program ###

# Fun Word game title
print(r"""
  ________                                __  .__            __                            .___
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__ _____ _/  |_  __  _  _____________  __| _/
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \\__  \\   __\ \ \/ \/ /  _ \_  __ \/ __ | 
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \/ __ \|  |    \     (  <_> )  | \/ /_/ | 
 \______  /____/  \___  >____  >____  >  |__| |___|  (____  /__|     \/\_/ \____/|__|  \____ | 
        \/            \/     \/     \/             \/     \/                                \/
""")

# Explain the rules of the game
print("Welcome to Guess That Word!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("You have six tries to get the word correct")
print("The word is SIX CHARACTERS long, and you must enter a guess of this length.")
print("If a letter is in the correct place, it will turn green")
print("If a letter is in the word but NOt in the correct place, it will turn yellow")
print("If the letter is NOT in the word, it will turn red")
print()
print("Good luck!")
print()

# Make sure the user's guess starts blank
userGuess = ""

# Decide what your secret word is
secret = "bottle"
count = 0

# Start asking the user to guess, but only allow six guesses.
while count < 6 and userGuess != secret: 
  userGuess = getUserGuess("")
  printGuessAccuracy(userGuess, secret)
  count += 1
  print()
  
# if they guess incorrectly six times, end the game
if count == 6:
    print("Sorry, you are out of guesses! You lose!")
  
# if they guess the word correctly, then tell them they won the game
if (userGuess == secret):
    print("You win!")
