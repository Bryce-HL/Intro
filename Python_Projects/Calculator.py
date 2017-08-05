# sign = raw_input()

'''
first = raw_input()

second = raw_input()

x = first

if x == first:
    x = int(first)

y = second

if y == second:
    y = int(second)
 

if x <= 10:
    print(x * y)
elif x >= 9:
    print(x + y)
'''

def my_calculator_function(x, y, z):
    if z == "add":
        print(x + y)
    elif z == "divide":
        print(x / y)
    elif z == "multiply":
        print(x * y)
    elif z == "subtract":
        print(x - y)

x = raw_input()

first = x

if first == x:
    first = int(x)

y = raw_input()

second = y

if second == y:
    second = int(y)

z = raw_input()

my_calculator_function(first, second, z)




