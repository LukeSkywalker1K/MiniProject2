'''
  

      HANGMAN LETTER GAME 


'''


# import external libraries
import random 

# make a list of words 

words = ['apple','banana','orange','coconut','strawberry','lime','grapefruit','lemon','kumquat','blueberry','melon']

while True:
    # ask user to start the game
    start = input("Press enter / return to start, or enter Q to quit")

    if start.lower() == 'q':
        break

    # pick a random word
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []
    
    
    # add condition for win or loose
    while len(bad_guesses) < 7 and len(good_guesses) != len (list( secret_word)):
        # draw  spaces
        # draw guessed letters, spaces and strikes
        for letter in secret_word:
            if letter in good_guesses:
                print ( letter , end='')
            else:
                print('_', end=' ')
                

        print('\nStrikes : {} / 7'.format(len(bad_guesses)))
        print ('')

        # take guess
        guess = input ("Guess a letter : ").lower()

        # Check the input from user for boundary conditions
        if  len(guess) != 1:
            print ("You can only guess a single letter !") 
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guess that letter")
            continue
        elif not guess.isalpha():
            print ("You can only guess letters !")
            continue
        
        # print out win / lose

        if guess in secret_word:
            good_guesses.append(guess)

        if len (good_guesses) == len ( list(secret_word)):
            print ("You win : The word was {}". format(secret_word))
            break
        else:
            bad_guesses.append(guess)
    
    else:   # else for the while, if you win, it will never be executed
        print ("You didn't guess it: my secret word was {}". format(secret_word))
