# Python Guessing Game

import random

# Guess the number the computer selected
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:
            print ('Sorry, guess again. Too high')
            
    print (f'Yay, congrats! You guessed the number {random_number} correctly')

# Computer will guess the number selected by the user
def computer_guess(x):
    computer_num = 0
    user_num = x
    upperlimit = x + 10
    lowerlimit = 1
 
    while computer_num != user_num:
        computer_num = random.randint(lowerlimit,upperlimit)
       
        if computer_num > x:
            print("Sorry, Too high:  ", computer_num)
            upperlimit = computer_num
        elif computer_num < x:
            print("Sorry Too low:  ", computer_num)
            lowerlimit = computer_num
    print(f'Yay, the computer guessed {computer_num}')

def Wanttoplay():
    while True:
        # Prompt the User to choose a guessing game
        print("Welcome to the guessing game")
        print("You have two options:")
        print(" 1.  You can guess the computer's number")
        print(" 2.  The computer can guess your number")
        print(" 3.  Quit")
        selectopt = input("Enter a selection:  ")
        
        #Process the option selected
        if selectopt == '1':
            secretnum  = random_number = random.randint(1,500)
            guess(secretnum)
        elif selectopt == '2':
            user_num = int(input("Enter a number for the computer to guess:  "))
            computer_guess(user_num)
        else:
            print("Bye")
            break
        
        #Does the User want to play again?
        action = input("Play Again (Y/N): ").upper()
        if action == 'Y':
            continue
        else:
            print("Thanks for playing")
            break

Wanttoplay()