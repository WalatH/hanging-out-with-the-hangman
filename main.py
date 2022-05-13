import random
print("Howdy partner, welcome to the gallows.")

words = ["Informatica", "Informatiekunde", "Spelletje", "Aardigheidje", "Scholier", "Fotografie", "Waardebepaling", "Specialiteit", "Verzekering", "Universiteit", "Heesterpark"]

rng = (random.choice(words))
number_of_letters = len(rng) - rng.count(" ")
print(number_of_letters)
print(rng)