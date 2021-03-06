print('Lab Exercise 08')

# class notes
# a_string  = "cats and dogs"
# print(a_string)
# print(type(a_string))


# a_list = [1,2,3]
# print(type(a_list))





#class Cat(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         descrp = f"{self.name} is {self.age} years old"
#         return descrp


# cat1 = Cat("LW", 12)
# print(cat1)







# LAB EXERCISE 08

# This lab exercise introduces you to classes, creating instances and updating variables. 

# PROBLEM 1 (5 Points)

# In this problem, you will
# 1) Create a class named Dog
# 2) Creata an __init__ function
# 3) Initialize variables


# BEGIN PROBLEM 1 SOLUTION

# A class named Dog has been created using the keyword class for you.
# You will be initiating the class with the init function


class Dog:
    '''
    This Dog class helps instantiate the Dog objects later in the lab exercise.
    This is your first exposure to Object Oriented Programming (OOP). This contains
    the init function and helper models. 
    '''
# Below is the __init__ function. You will initialize the class with <name> and an
# empty list called <tricks>. Add <name> and <age> as your function parameter and initialize <name>
# with <name> and <age> with <age>. Also initialize <tricks> as an empty list.
    def __init__(self, name, age):
        '''
        This function initialises the class with three variables: <name>, <age> and <tricks>.
        <name> is updated using the passed positional argument <name> and <age> is updated with
        <age>. <tricks> is initilized as an empty list.

        parameters:
            name (string): Name of the Dog for the instance.
            age (float): Age od the Dog for the instance.

        returns:
            none 
        '''
        self.name = name
        self.age = age
        self.tricks = []


# END PROBLEM 1 SOLUTION

# PROBLEM 2 (2.5 Points)
# In this problem you will
# 1) Create a methond to update class variable

# BEGIN PROBLEM 2 SOLUTION

# Create a function called <increment_age> to increment age of the dog.

    def increment_age(self):
        '''
        This function updates the <age> class variable's value by 1.

        paraments:
            none
        
        returns:
            none
        '''
        self.age = self.age + 1


# PROBLEM 3 (5 Points)
# In this problem you will 
# 1) Create a helper function
# 2) Use a positional argument to update class instance

# BEGIN PROBLEM 3 SOLUTION

# Create a function called <update_tricks> that takes in positional argument <trick>
# and appends the value to the <tricks> list.

    def update_tricks(self, trick):
        '''
        This function updates the <tricks> list with the value provided from the
        <trick> argument. Append <trick> to <tricks>.

        parameters:
            trick (string): New trick to add to the instace.
        
        returns:
            none
        '''
        self.tricks.append(trick)
# END PROBLEM 3 SOLUTION

# PROBLEM 4 (2.5 Points)
# In this problem you will
# 1) Override the __str__ function to represent the dog class

# BEGIN PROBLEM 4 SOLUTION

# Create a function called __str__ to return the string representation of the object.
    def __str__(self):
            '''
            This function returns the string representation of the object.

            parameters:
                none
            returns:
                string: the string representation of the object. This should 
                return the following string "Dog(name = <name>, age = <age>, tricks = <tricks>)"
            '''
            string = f"Dog(name = {self.name}, age = {self.age}, tricks = {self.tricks})"
            return string


# END PROBLEM 4 SOLUTION


# PROBLEM 5 (5 Points)
# In this problem, you will
# 1) Instantiate an object
# 3) Update the instance's variables.

# BEGIN PROBLEM 5 SOLUTION

#  set "Fido" to a variable named <name>.
name = "Fido"

# set "3" to a variable named <age>. Do not set it as a string.
age = 3
# Instantiate a Dog object with <name> and <age> and assign it to a variable named <my_dog>.
dog = Dog(name, age)
print(dog)
# Call <incerement_age>.
dog.increment_age()
print(dog)
dog2 = Dog(name,age)
print(dog2)
# Call <update_tricks> and pass "sit" as a keyword argument.
dog.update_tricks("sit")
print(dog)
# call the object representation using <__str__> method and save it to variable <string>.
#string = dog.__str__()
string = str(dog)

#print <string>
print(string)

# END PROBLEM 5 SOLUTION

# END LAB EXERCISE
