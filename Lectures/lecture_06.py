from datetime import datetime

# Variable with global scope (available to all functions below)
TODAY = datetime.today().isoformat() # constant (capitalized)

# Week 04 Objectives
# 1. Define and call a function that accepts arguments and returns a value
# 2. Understand variable scope (global / local)
# 3. Employ conditional statements to control execution
# 4. Write expressions using arithemtic, assignment, comparison
#    logical, identity, and membership operators
# 5. Respond to tracebacks and error types (debugging)
#    e.g., AttributeError, IndentionError, NameError, TypeError
# 6. Read and comprehend a function's Docstring


# 1.0 FUNCTIONS

# Basic anatomy (no parameters, implicit return None)
def greeting_v01():
    print('Nǐ hǎo') # function must be called to print greeting

# UNCOMMENT
# Call a function
greeting_v01()

# UNCOMMENT
# IndentionError: Indention matters
def greeting():
    print('Hello') # indent 4 spaces or raise IndentionError


# Define a function with a parameter and a return statement
def greeting_v02(first_name):
    return "Nǐ hǎo {}".format(first_name) # str.format()


# Call function, pass argument, assign return value to variable
first_name = 'Max'
hello = greeting_v02(first_name)

print(f"greeting_v02 = {hello}\n") # f-string


# Define a function with two parameters
def greeting_v03(first_name, last_name):
    return f"Nǐ hǎo {first_name} {last_name}\n" # f-string


# Call function, pass arguments, assign return value to variable
last_name = 'Zhang'

hello = greeting_v03(first_name, last_name) # positional args

print(f"greeting_v03 = {hello}\n") # f-string

# Call function using keyword arguments
hello = greeting_v03(last_name=last_name, first_name=first_name) # order doesn't matter

print(f"greeting_v03_keyword_args = {hello}\n") # f-string


# Define function with optional parameter and default value
def greeting_v04(first_name, last_name, role='GSI'):
    return f"Nǐ hǎo {first_name} {last_name}, {role}\n" # f-string


# Call function without passing optional argument
first_name = 'Yangtao' # variable reassignment

hello = greeting_v04(last_name, first_name) # reverse order

print(f"greeting_v04 = {hello}\n") # f-string


# Call function passing optional argument
first_name = 'Morgan'
last_name = 'Durow'
role = 'Graduate Student Instructor'

hello = greeting_v04(first_name, last_name, role) # optional arg passed

print(f"greeting_v04 = {hello}\n") # f-string


# Define function with locally scoped variable
def greeting_v05(first_name, last_name, role='GSI'):
    now = datetime.today().isoformat() # can't reference outside function
    return f"Nǐ hǎo {first_name} {last_name}, {role}, {now}\n" # f-string

hello = greeting_v05(first_name, last_name)

print(f"greeting_v05 = {hello}\n") # f-string

# NameError: now datetime object is not referenceable (UNCOMMENT)
#print(f"now = {now}\n")

# Function references a global variable (TODAY)
def greeting_v06(first_name, last_name, role='GSI'):
    return f"Nǐ hǎo {first_name} {last_name}, {role}, {TODAY}\n" # bad practice

first_name = 'Andrew'
last_name = 'Vande Guchte'

hello = greeting_v06(first_name, last_name)
print(f"greeting_v06 = {hello}\n") # f-string

# Function references a non-locally scoped variable (status)
status = 'MSI (2nd year)'
def greeting_v07(first_name, last_name, role='GSI'):
    return f"Nǐ hǎo {first_name} {last_name}, {role}, {status}\n" # bad practice

hello = greeting_v07(first_name, last_name) # refactor function to accept status

print(f"greeting_v07 = {hello}\n") # f-string


# Function refactored to accept passed in status and datetime values
def greeting_v08(first_name, last_name, role='GSI', status='MSI (1st year)', date_time=TODAY):
    return f"Nǐ hǎo {first_name} {last_name}, {role}, {status}, {date_time}\n"

hello = greeting_v08(first_name, last_name, status=status) # keyword arg required

print(f"greeting_v08 = {hello}\n") # f-string


# 2.0 CONDITIONAL STATEMENTS

# Note: the % (modulo) operator divides the first operand 
# by the second and returns the remainder.

# Conditional execution (if)
num = 507

# UNCOMMENT
if num % 2 == 0: # print() will only be called if expression evaluate to True
   print(f"Conditional execution: {num} is an even number\n")


# Alternative execution (if-else)
num = 506

# UNCOMMENT
if num % 2 == 0:
   print(f"Alternative execution: {num} is an even number\n")
else:
   print(f"Alternative execution: {num} is an odd number\n")


# Chained execution (if-elif-else)
x = 10 * 10 + 5 // 2    # floor division
y = 10 * (10 + 5) // 2  # floor division

# UNCOMMENT
if x > y:
    print(f"Chained execution: {x} is greater than {y}\n")
elif x < y:
    print(f"Chained execution: {x} is less than {y}\n")
else: 
    print(f"Chained execution: {x} equals {y}\n")

# 3.0 FUNCTION REFACTORING

# Function v01 features
# 1. Docstring (describes function)
# 2. Locally scoped variable (is_even)
# 3. Conditional statement (if)
# 4. Modulo operator (%), operands expression
# 5. Return statement

def is_int_even_v01(num):
    """
    Use the modulo operator to evaluate whether an integer provided by
    the caller is even or odd, returning either True or False.

    Parameters:
        num (int): the integer to be evaluated.

    Returns:
        is_even (boolean): True or False depending on the modulo check
    """

    is_even = False     # locally scoped variable

    if num % 2 == 0:    # conditional check
        is_even = True

    return is_even      # return statement


# Call the function and assign return value
is_even = is_int_even_v01(506)
print("is_int_even_v01 is_even = {} \n".format(is_even)) # str.format()

# Call the function and assign return value
is_even = is_int_even_v01(507)
print(f"is_int_even_v01 is_even = {is_even}\n") # f-string


# Function v02 changes (whoa two return statements)
# 1. Locally scoped variable eliminated
# 2. Condtional statement determines choice of return statement

def is_int_even_v02(num):
    """
    Use the modulo operator to evaluate whether an integer provided by
    the caller is even or odd, returning either True or False.

    Parameters:
        num (int): the integer to be evaluated.

    Returns:
        is_even (boolean): True or False depending on the modulo check
    """

    if num % 2 == 0:
        return True         # return statement
    else:
        return False        # return statement


# Call the function and assign return value
is_even = is_int_even_v02(14)
print(f"is_int_even_v02 is_even = {is_even}\n")

# Call the function and assign return value
is_even = is_int_even_v02(27)
print(f"is_int_even_v02 is_even = {is_even}\n")


# Function v03 changes (return statement only)
# 1. Any object can be used to test the "truth value"
# 2. Expression num % 2 == 0 possesses a truth value
# 3. We can test the "truth_value" and return the result immediately

def is_int_even_v03(num):
    """
    Use the modulo operator to evaluate whether an integer provided by
    the caller is even or odd, returning either True or False.

    Parameters:
        num (int): the integer to be evaluated.

    Returns:
        is_even (boolean): True or False depending on the modulo check
    """

    return num % 2 == 0     # truth value test


# Call the function and assign return value
is_even = is_int_even_v03(0)
print(f"is_int_even_v03 is_even = {is_even}\n")

# Call the function and assign return value
is_even = is_int_even_v03(-5)
print(f"is_int_even_v03 is_even = {is_even}\n")


# DELIBERATELY RAISE AN EXCEPTION (UNCOMMENT)
#is_even = is_int_even_v03('24') # pass in string


# Function v04 changes (try / except blocks)
# 1. Introduce exception handling with try / except blocks
# 2. Catch TypeError exceptions and return False

def is_int_even_v04(num):
    """
    Use the modulo operator to evaluate whether an integer provided by
    the caller is even or odd, returning either True or False. Wrap
    return statements in try / except blocks to catch exceptions.

    Parameters:
        num (int): the integer to be evaluated.

    Returns:
        is_even (boolean): True or False depending on the modulo check
    """

    try:
        return num % 2 == 0     # truth value test
    except:
        return False

    # try:
    #     return num % 2 == 0
    # except TypeError:          # specify specific error type
    #     return False

    # try:
    #     return num % 2 == 0
    # except (ValueError, TypeError):  # specify multiple error types in a tuple
    #     return False


# Check if try / except blocks catch the exception and return False
is_even = is_int_even_v04('12') # triggers TypeError
print(f"is_int_even_v04 is_even = {is_even}\n")

is_even = is_int_even_v04('five') # triggers TypeError
print(f"is_int_even_v04 is_even = {is_even}\n")
