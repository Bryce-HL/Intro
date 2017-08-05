
'''
this function adds two numbers
'''

def my_add_function(first_number, second_number):
    print(first_number + second_number)

'''
this function is for multiplying two numbers
'''

def my_multiply_function(first_number1, second_number1):
    print(first_number1 * second_number1)
    
'''
this function is for subtracting two numbers
'''

def my_subtraction_function(first_number2, second_number2):
    print(first_number2 - second_number2)

'''
this function is for dividing two numbers
'''

def my_division_function(first_number3, second_number3):
    print(first_number3 / second_number3)

'''
more advanced function
'''

def my_smart_function(first_number4, second_number4, math_operation):
    if math_operation == "add":
        print(first_number4 + second_number4)
    elif math_operation == "multiply":
        print(first_number4 * second_number4)
    elif math_operation == "divide":
        print(first_number4 / second_number4)
    elif math_operation == "subtract":
        print(first_number4 - second_number4)



my_add_function(3, 8)

my_multiply_function(5, 2)

my_subtraction_function(5, 2)

my_division_function(32, 4)

my_smart_function(99, 3, "divide")

my_smart_function(76, 26, "subtract")

my_smart_function(23, 22, "add")

my_smart_function(3, 9, "multiply")









