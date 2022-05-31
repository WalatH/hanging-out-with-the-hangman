import random
import os

isGameRunning = True

def pressEnter():
    input("Press enter to continue...")
    os.system('clear')

def game():
    guesses = 0
    rng = (random.choice(words))
    number_of_letters = len(rng)
    guessedWord = list(rng)
    underscore = ("_ " * spaces)
    wrong_list = []




print("Howdy partner, welcome to the gallows. You tryin' to hang out with me?")    
pressEnter()

words = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterpark"]

rng = (random.choice(words))
number_of_letters = len(rng)
guessedWord = list(rng)

spaces = len(rng)
underscore = ("_ " * spaces)
print(underscore)
print(rng)
print(guessedWord)


#while isGameRunning == True:
