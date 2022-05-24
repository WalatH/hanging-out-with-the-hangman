import random
import os


def pressEnter():
    input("Welcome to 'Hanging out with the Hangman!' Press enter to continue...")
    os.system('clear')

print("Howdy partner, welcome to the gallows. Lets HANG out!")    
def pressEnter():
    input("Press enter to continue...")
    os.system('clear')

words = ["Informatica", "Informatiekunde", "Spelletje", "Aardigheidje", "Scholier", "Fotografie", "Waardebepaling", "Specialiteit", "Verzekering", "Universiteit", "Heesterpark"]

rng = (random.choice(words))
number_of_letters = len(rng)

spaces = len(rng)
underscore = ("_ " * spaces)
print(underscore)

for i in range(len(rng)):
    letter = input("Guess a letter! ")
    if letter in rng:
        print ("Correct",letter)
    elif letter not in rng:
        print("Wrong!")

    

print(number_of_letters)
print(rng)
