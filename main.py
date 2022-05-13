import random
print("Howdy partner, welcome to the gallows. You tryin' to hang out with me?")

words = ["Informatica", "Informatiekunde", "Spelletje", "Aardigheidje", "Scholier", "Fotografie", "Waardebepaling", "Specialiteit", "Verzekering", "Universiteit", "Heesterpark"]

rng = (random.choice(words))
number_of_letters = len(rng) - rng.count(" ")

space = len(rng)
underscore = ("_ " * space)
print(underscore)

for i in range(1, 9):
    letter = input("Guess a letter ")
    if letter in rng:
        print ("Correct",letter)
    else:
        print ("Incorrect", " ",letter)
      
print(number_of_letters)
print(rng)
