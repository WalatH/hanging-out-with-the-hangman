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

def hangMan():
  guesses = 0					
  word = selectWord()				
  word_list = list(word)	
  blanks = "_"*len(word)	
  blanks_list = list(blanks) 
  new_blanks_list = list(blanks)
  guess_list = []

  print("Howdy partner, welcome to the gallows. You tryin' to hang out with me?")
  pressEnter()
  print("Welcome to Hangman, made by Mikail and Walat. Have fun and remember kids do not cheat or else I will hunt you down... Anyways have fun!")
  print("\n")
  name = input("Enter your name: ")
  print("\n\nYour name is " + name + "? Are you a 100% sure? Alright, good luck.\n\n\n")
  pressEnter()
  print ("LETS DO THIS!\n\n")
  hangman(guesses, word)
  print ("\n")
  print ("" + ' '.join(blanks_list))
  print ("\n")
  print ("Guess a letter.\n\n")

  while guesses < 6:
  
  		guess = str(input(" >"))
  		guess = guess.lower()
  		
  		if len(guess) > 1:
  				print ("\n\nSTOP CHEATING DO YOU WANT ME TO HUNT YOU DOWN?! Enter ONE letter at time!       PLEASE.\n\n")
      elif guess == "":
  				print ("\n\nDon't you want to play? Enter one letter at a time.\n\n")
  		elif guess in guess_list:
  				print ("\n\nYou already guessed that letter! DONT YOU REMEMBER?! Here is what you've already guessed!:\n\n")
  				print (' '.join(guess_list))
  		else:
  				guess_list.append(guess)
  				i = 0
  				while i < len(word):
  						if guess == word[i]:
  								new_blanks_list[i] = word_list[i]
  						i = i+1