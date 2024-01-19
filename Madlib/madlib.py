#  Madlib game


def madlibmenu():
    print("")
    print("-------------------------------------------")
    print("|  Welcome to Madlibs!                    |")
    print("|  Choose a madlib and follow the prompts |")
    print("|  Read the story you created             |")
    print("|                                         |")
    print("|  1. Playing Golf                        |")
    print("|  2. A vist to the park                  |")
    print("|  3. Working in a factory                |")
    print("|  4. Trip to Mars                        |")
    print("|  5. Trip to the Pyramids                |")
    print("|  6. A visit to a restaurant             |")
    print("|  0.  Quit                               |")
    print("-------------------------------------------")
    print("")
    
def madlib1():
    # Playing golf
    adjective = input("Adjective:  ")
    verb = input("Verb: ")
    animal1 = input("Animal:  ")
    animal2 = input("Another Animal: ")

    matlib1 = f"Golf is so {adjective}.  It makes me so excited all the time because I love to {verb}. One time while I was golfing a really large {animal1} walked across the course.  Even the {animal2} stopped to watch."
    print("")
    print(matlib1)
    
def madlib2():
    # A visit to a park
    noun = input("Noun: ")
    noun2 = input("Another noun: ")
    name = input("Name: ")
    pronoun = input("Pronoun: ")
    animal = input("Animal:  ")
    plural_noun = input("Plural noun: ")
    sport =  input("Sport:  ")
    
    madlib2 = f"In the city of {noun}, there is a park called {noun2}.  {name} likes to walk {pronoun} {animal} in the park.  Today, {name} saw a group of {plural_noun} playing {sport}."
    print("")
    print(madlib2)
    
def madlib3():
    # Working in a factory
    name1 = input("Name: ")
    name2 = input("Another Name: ")
    food = input("Food: ")
    adjective = input("Adjective: ")
    noun = input("Noun: ")
    
    madlib3 = f"{name1} and {name2} got a job in a {food} factory.  At first, they thought it was an {adjective} job.  When the {noun} came to inspect their work, the {noun} approved of their progress.  The {noun} requested more work for {name1} and {name2}."
    print("")
    print(madlib3)
    
def madlib4():
    # Trip to Mars
    adjective = input("Adjective:  ")
    adjective2 = input("Another adjective:   ")
    adjective3 = input("Another adjective:  ")
    noun = input("Noun:  ")
    animal = input("Animal:  ")
    plural_noun = input("Plural noun: ")
                      
    madlib4 = f"Today, I went on a trip to Mars with my {adjective} family. We packed our {noun} and boarded the {adjective} rocket. During the journey, we saw lots of {plural_noun} and even spotted a {animal} floating in space. When we arrived, we explored the {adjective2} terrain and found a secret cave filled with {noun}. Overall, our trip to Mars was {adjective3} and unforgettable!"
    print("")
    print(madlib4)
    
def madlib5():
    # Trip to pyramids
    adjective = input("Adjective: ")
    adjective2 = input("Another adjective:  ")
    adjective3 = input("Another adjective:  ")
    noun = input("Noun:  ")
    color = input("Color:  ")
    animal = input("Animal: ")
    a_place = input("A place: ")
    
    madlib5 = f"One day, I went on a(n) {adjective} trip to the pyramids in {a_place}. I packed my favorite {noun} and my lucky {color} hat. When we arrived, I was amazed by the {adjective2} size of the pyramids. I even saw a(n) {animal} near the pyramids! It was a(n) {adjective3} day filled with excitement and adventure."
    print("")
    print(madlib5)
    
def madlib6():
    # Visiting a restaurant
    adjective = input("Adjective:  ")
    noun = input("Noun:  ")
    game = input("Game: ")
    food = input("Food:  ")
    food2 = input("Another Food:  ")
    adjective2 = input("Another Adjective: ")
    
    madlib6 = f"Once upon a time, I went to a {adjective} restaurant with my friends. When the waiter brought the menu, I couldn't decide what to order. I finally chose the {food} and it was so {adjective2}! While we waited for our food, we played {game} and laughed a lot. When the dessert came, I had the most delicious {food2} I've ever tasted. It was a fun day at the restaurant!"
    print("")
    print(madlib6)
    
def main():
    while True:
        madlibmenu()
        prompt = input("Enter your selection:  ")
        try:
            if   prompt == '0':
                print("Bye!")
                break
            elif prompt == '1':
                madlib1()
            elif prompt == '2':
                madlib2()
            elif prompt == '3':
                madlib3()
            elif prompt == '4':
                madlib4()
            elif prompt == '5':
                madlib5()
            elif prompt == '6':
                madlib6()
            else: print("You entered an invalid option")
        except:
            print("OOps, something went wrong")

main()