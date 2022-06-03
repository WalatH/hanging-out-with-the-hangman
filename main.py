import random
import os

def hangman(guesses, wd):
		if (guesses == 0):
				print ("_________                6 lives left")
				print ("|	 |")
				print ("|")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (guesses == 1):
				print ("_________                5 lives left")
				print ("|	 |")
				print ("|	 O")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (guesses == 2):
				print ("_________                4 lives left")
				print ("|	 |")
				print ("|	 O")
				print ("|	 |")
				print ("|")
				print ("|")
				print ("|________")
		elif (guesses == 3):
				print ("_________                3 lives left")
				print ("|	 |")
				print ("|	 O")
				print ("|	/|")
				print ("|")
				print ("|")
				print ("|________")
		elif (guesses == 4):
				print ("_________                2 lives left")
				print ("|	 |")
				print ("|	 O")
				print ("|	/|\ ")
				print ("|")
				print ("|")
				print ("|________")
		elif (guesses == 5):
				print ("_________                1 life left")
				print ("|	 |")
				print ("|	 O")
				print ("|	/|\ ")
				print ("|	/")
				print ("|")
				print ("|________")
		elif (guesses == 6):
				print ("_________                0 lives left")
				print ("|	 |")
				print ("|	 O")
				print ("|	/|\ ")
				print ("|	/ \ ")
				print ("|	")
				print ("|________")
				print ("\n")
				print ("The word was %s." %wd)
				print ("\n")
				print ("\n'You have killed him... How do you feel? He had a family, and you decide to just kill him? Shame on you! Next time you should try your best!'")
				print ("\nWould you like to play again, type ja if you WANT to play again and type nee if you DON'T want  to play again.")
				again = str(input("> "))
				again = again.lower()
				if again == "ja":
				  hangMan()
				return
      
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
          
          if new_blanks_list == blanks_list:
  						print ("\n\nYour letter isn't in this word.\n\n")
  						guesses = guesses + 1
  						hangman(guesses, word)
  						
  						if guesses < 6:
  								print ("\n\nTry again.\n\n")
  								print (' '.join(blanks_list))
  						
  				elif word_list != blanks_list:
  						
  						blanks_list = new_blanks_list[:]
  						print (' '.join(blanks_list))
            
              if word_list == blanks_list:
  						  print ("\n\nYOU WIN! YOU SAVED ME, I CAN'T THANK YOU ENOUGH\n\n")
  						  print ("\n\n")
  						  print ("\n\nWould you like to play again?\n\n")
  						  print ("\n\nType ja if you want to play again and type nee if you DON'T want to play again\n\n")
  						  again = str(input("> "))
  						  if again == "nee":
  						    hangMan()
  						  exit()

  						else:
  								print ("\n\nGreat guess! Guess another letter!\n\n")
												
hangMan()