#!/usr/bin/env python
# coding: utf-8


# Mini python game
# Ask the user a series of questions
# Provide the user with a tally of the number of 
# questions answered correctly.
# Provide the user with the correct answer for
# incorrectly answered questions

def prompt(question, answer):
    global score
    response = input(question).lower()

    if response == answer:
        print("correct!")
        score += 1
    else: 
        print("incorrect!, the correct answer is ",answer)

# Greet the user
print("Welcome to my game!")

# Ask user if the user wants to play

answer  = input("Do you want to play?:  ").lower()
if answer == 'yes':
    print("great!  Let's see how many questions you can answer correctly.")
    #initialize score
    score = 0
    
    # question 1
    prompt("In which city is the Liberty Bell located?",                "philadelphia")
   
    # question 2
    prompt("which borough in NYC is located on the U.S. mainland",            "bronx")
    # question 3
    prompt("This pet uses a scratching post","cat")
    
    # question 4
    prompt("Southern bread made from corn","cornbread")
    
    # question 5
    prompt("Name of the K-pop group that addressed the United Nations","bts")
    
    # question 6
    prompt("Roy G Biv describes the colors of what?","rainbow")
    
    #question 7
    prompt("Many backyard birds love the seeds of this flower","sunflower")
    
    # question 8
    prompt("Which singer made the song Proud Mary famous?", "tina turner")
    
    # no more questions
    print("that was the last question")
    print("You answered ",score," questions correctly out of 8")
    print("Bye!")
else:
    print("Bye!")
    
    

          
          
          


