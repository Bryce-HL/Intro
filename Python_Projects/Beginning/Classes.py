class Person:

    def __init__(self, name, height, hair_color):
        self.name = name
        self.height = height
        self.hair_color = hair_color

    def print_name(self):
        print(self.name)

    def print_height(self):
        print(self.height)

    def print_hair_color(self):
        print(self.hair_color)

Bryce = Person("Bryce Helmbrecht-Lommel", "5-11.25", "Blonde/Red")
Peter = Person("Peter Lommel", "6-2", "Brown")

'''
Bryce.print_name()
Bryce.print_hair_color()
Bryce.print_height()

Peter.print_name()
Peter.print_hair_color()
Peter.print_height()
'''

# This is sub-classing

class Employee(Person):
    def __init__(self, name, height, hair_color, employee_id):
        Person.__init__(self, name, height, hair_color)
        self.employee_id = employee_id

    def print_employee_id(self):
        print(self.employee_id)


billy_the_employee = Employee("Billy", "5-5", "Blonde", "a123")

billy_the_employee.print_name()
billy_the_employee.print_hair_color()
billy_the_employee.print_height()
billy_the_employee.print_employee_id()




