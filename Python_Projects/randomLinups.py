from random import sample, randint
from advancedClassProject import Rower


print('''
Bryce = 1
Peter = 2
Bill = 3
Bob = 4
Joe = 5
Jim = 6
John = 7
Jack = 8
Cory = 9
Dylan = 10
Fred = 11
''')

print(sample(xrange(1, 9),8))
print('''randint(9, 11)
''')

'''
print(randint(1, 8))
print(randint(1, 8))
print(randint(1, 8))
print(randint(1, 8))
print(randint(1, 8))
print(randint(1, 8))
print(randint(1, 8))
print(randint(1, 8))
print(randint(9, 10))
'''

Bryce = Rower("Bryce", "Both")
Peter = Rower("Peter", "Both")
Billy = Rower("Billy", "Port")
Joe = Rower("Joe", "Starboard")
Bob = Rower("Bob", "Coxswain")

Bryce.print_rower()
Peter.print_rower()
Billy.print_rower()
Joe.print_rower()
Bob.print_rower()
