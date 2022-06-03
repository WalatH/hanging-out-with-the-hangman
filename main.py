import random
import os


def selectWord():
  file = open('WordsGame')
  words = file.readlines() 
  myword = 'a'
  while len(myword) < 4:
    myword = random.choice(words)
    myword = str(myword).strip('[]')
    myword = str(myword).strip("''")
    myword = str(myword).strip("\n")
    myword = str(myword).strip("\r")
  myword = myword.lower()
  return myword
def pressEnter():
  input("Press enter to continue...")
  os.system('clear')

  



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
