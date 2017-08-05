import sys

print("What is your name?")

name = raw_input()

hello = "Hello " 

story1 = '''. Thank you for playing, this is a trivia game where in order to proceed 
you must get the answer correct, if you answer falsely the game will end and
you will be brought back to the beginning. Please remember, capitalization is important
type your answer exactly as you see. Do you understand? Type yes or no.
'''

print(hello + name + story1)

Answer1 = raw_input()

if Answer1 == "yes":
    print('''
    Question 1:
    Frankenstein was the monster.
    Type true or false.
    ''')

elif Answer1 == "no":
    print("I'm sorry to hear that, I hope you will try again.")
    sys.exit(1)

Answer2 = raw_input()

if Answer2 == "true":
    print("I'm sorry, Frankenstein was the scientist. You were wrong.")
    sys.exit(1)
elif Answer2 == "false":
    print('''
    Correct!
    Question 2:
    Blah Blah Blah
    ''')