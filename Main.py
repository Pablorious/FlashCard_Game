import pickle
import os

class Card:
    def __init__(self, face, back):
        self.face = face
        self.back = back

running = True
cards = []
amountwrong = 0
os.system('clear')

print("Welcome to Pablo's Flashcard Simulator alpha 0.09!")
print("")
print("Now without aliases in the start command!")
print("Type \"help\" for a list of commands")

try:
    cards = pickle.load(open('cards.pk', 'rb'))
except IOError:
        print("woops! no cards!")

while(running):
    try: 
        answer = input(">>> ")
    except KeyboardInterrupt:
        answer = "quit"

    if answer == "load":
        print("what cards do you want to load?")
        answer = input("...>>> ")
        
        try:
            cards = pickle.load(open(answer,'rb'))
        except IOError:
            print("no cards with that name")

    if answer == "help":
        print("help:-----display a list of commands")
        print("quit:-----exit the program")
        print("load------load your cards") 
        print("ls--------list your cards") 
        print("saveas----save your cards")
        print("start:----begin a flash card round")
        print("clear:----clear the screen") 
        print("rmcard:---delete a card") 
        print("mkcard:---make a new card")

    if answer == "quit":
        running = False
    
    if answer == "saveas":
        answer = input("...>>> ")
        pickle.dump(cards,open(answer,'wp'),pickle.HIGHEST_PROTOCOL)

    if answer == "clear":
        os.system('clear')
    
    if answer == "ls":
        i = 0
        for card in cards:
            print(str(i)+  " " + card.face + "," + card.back)
            i += 1

    if answer == "rmcard":
        print("type the cards number to delete it, type -1 to cancel")
           
        answer = input("...>>> ")  
        
        try:
            answer = int(answer)
        except ValueError:
            print("invalid input")
        
        if answer != -1 and answer >= 0 and answer <= len(cards):
            try:
                cards.pop(answer)
            except IndexError:
                print("that card does not exist")

    if answer == "mkcard":
        print("Enter the cards front and back")
        cards.append(Card(input("...>>> "),input("...>>> ")))
    
    if answer == "start": 
        amountwrong = 1
        while amountwrong > 0:
            amountwrong = 0
            startcards = cards[:] 
            
            while len(startcards) > 0: 
                purge = []
                for i,card in enumerate(startcards): 
                    os.system('clear')
                
                    print(card.face)
                    answer = input("...>>> ")
                
                    os.system('clear')
                    print("Card.face:        :" + card.face)
                    print("Card.back         :" + card.back)
                    print("answer:           :" + answer)
            
                    print("did you get it right? (y/n)")

                    answer = input("...>>> ")
                
                    if answer == "y":
                        purge.append(i)

                    if answer != "y" and answer != "n":
                        amountwrong += 1 
                    if answer == "n":
                        amountwrong += 1

                for i in reversed(purge):
                    del startcards[i]
