import random
import os
from time import sleep

def pressEnter():
    input("Press enter to continue...")
    os.system('clear')

print("Howdy partner, welcome to the gallows. You tryin' to hang out with me?")    
pressEnter()

words = ["Informatica", "Informatiekunde", "Spelletje", "Aardigheidje", "Scholier", "Fotografie", "Waardebepaling", "Specialiteit", "Verzekering", "Universiteit", "Heesterpark"]

rng = (random.choice(words))
number_of_letters = len(rng)

space = len(rng)
underscore = ("_ " * space)
print(underscore)

for i in range(5):
    letter = input("Guess a letter")
    if letter in rng:
        print ("Correct",letter)
    else:
        print ("Incorrect",letter)

      
print(number_of_letters)
print(rng)
