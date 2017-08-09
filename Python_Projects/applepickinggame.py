import time
import sys
global apples
global gold

apples = 0
gold = 0

def start():
    print('Hello and welcome!')
    name = raw_input('What is your name?')
    print"Thanks for playing", name, "your goal is to pick and sell apples."
    choice = raw_input("Do you wish to play?Y/N")
    if choice == "Y":
        print"Excellent"
        begin()
    elif choice == "N":
        print"Darn, okay then bye."
        sys.exit(1)


def begin():
    global apples
    global gold
    if gold > 99:
        print"You win, congrats."
        again = raw_input("Would you like to play again?Y/N")
        if again == "Y":
            print "Awesome!"
            start()
        elif again == "N":
            print"Thank you for playing!!"
            sys.exit(1)
    elif gold < 99:
        apple = raw_input("Would you like to pick an apple?Y/N")
        if apple == "Y":
            print"You pick an apple"
            apples = apples + 1
            print"You now have", apples, "apples."
            begin()
        elif apple == "N":
            if gold + apples == 0:
                print"You have nothing to do. You lose!"
                sys.exit(1)
            elif gold + apples > 0:
                sell = raw_input("Would you like to sell your apples?Y/N")
                if sell == "Y":
                    money = apples*10
                    gold = money
                    apples = 0
                    print"You now have 0 apples and", gold, "gold."
                    gold = money
                    begin()
      

start()

