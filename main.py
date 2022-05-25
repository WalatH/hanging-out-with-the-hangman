import random
import os

isGameRunning = True

def pressEnter():
    input("Press enter to continue...")
    os.system('clear')

lives = 6
    
print("Howdy partner, welcome to the gallows. You tryin' to hang out with me?")    
pressEnter()

words = ["Informatica", "Informatiekunde", "Spelletje", "Aardigheidje", "Scholier", "Fotografie", "Waardebepaling", "Specialiteit", "Verzekering", "Universiteit", "Heesterpark"]

rng = (random.choice(words))
number_of_letters = len(rng)
guessedWord = list(rng)

spaces = len(rng)
underscore = ("_ " * spaces)
print(underscore)
print(rng)
print(guessedWord)

for i in range(len(rng)):
    letter = input("Guess a letter ")
    if letter in rng:
        print ("Correct",letter)
    else:
        print ("Incorrect",letter)

while isGameRunning == True:
    if lives == 0:
        pass
    

print(number_of_letters)
print(rng)
