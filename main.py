import random
import os

def pressEnter():
    input("Press enter to continue...")
    os.system('clear')

print("Howdy partner, welcome to the gallows. You tryin' to hang out with me?")    
pressEnter()

words = ["Informatica", "Informatiekunde", "Spelletje", "Aardigheidje", "Scholier", "Fotografie", "Waardebepaling", "Specialiteit", "Verzekering", "Universiteit", "Heesterpark"]

rng = (random.choice(words))
number_of_letters = len(rng)

spaces = len(rng)
underscore = ("_ " * spaces)
print(underscore)
print(rng)

for i in range(len(rng)):
    letter = input("Guess a letter ")
    if letter in rng:
        print ("Correct",letter)
    else:
        print ("Incorrect",letter)


print(number_of_letters)
print(rng)
