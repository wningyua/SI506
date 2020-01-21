# SI 506 Lecture 04

# 1. DATA TYPES (introduced in SI 506)

# Values can be distinguished by their type.
# type(<expression>): built-in function for determining the type of a value or expression.

# string (sequence, immutable)
value = 'Spam'
print(type(value))

value = '5.2' # Beware (still a string)
print(type(value))

# integer (numeric)
value = 506
print(type(value))

# float (numeric)
value = 5.2
print(type(value))

# boolean
value = True
print(type(value))

value = False
print(type(value))

# list (sequence, mutable)
values = ['Egg', 'Bacon', 'Spam']
print(type(values))

# tuple (sequence, immutable)
values = ('Windows 10', 'macOS', 'Linux')
print(type(values))

# dictionary (map, mutable)
value = {'city': 'Ann Arbor', 'population': 127477}
print(type(value))


# 2. OPERATORS AND OPERANDS

# Operator: a special symbol that represents a computation.

# Note: Python includes a number of operator groups. Today we focus on Arithmetic operators.
# See https://www.w3schools.com/python/python_operators.asp for a quick overview.

# Operand: the object of a mathematical operation; 
# the object or quantity operated on by the operator.

x = 2 * 4 # the values two (2) and four (4) are operands.

# Arithmetic operators

# Addition (+)
x = 5 + 3

# Subtraction (-)
x = 5 - 3

# Multiplication (*)
x = 5 * 3

# Division a.k.a floating point division (/)
x = 5 / 3

# Floor division a.k.a integer division (//)
x = 5 // 2

# Floor division gotchas
x = 10.5 // 3                # float // int returns float
y = 10 // 3.5                # int // float returns float

# Modulo (remainder)
x = 5 % 2
y = 6 % 2
z = 7 % 2

# Exponentation
x = 5**2 # squared


# 3. OPERATOR PRECEDENCE

# Think PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

x = 10 / 5 + 5
y = 10 / (5 + 5)

print(x == y) # truth value test

a = 20
b = 10

c = a + b / 2  # average of two numbers?
d = (a + b) / 2 # average of two numbers?

print(c == d) # truth value test

x = 4**2 + 4 + 4 * 2 - 1
y = 4**2 + 4 * 2 + 3

print(x == y)


# 4. EXPRESSIONS

# "A piece of syntax which can be evaluated to some value."

# Examples of expressions
506                         # an integer value
506 + 507                   # an equation (operator and operands)
'Hello SI 506'              # a string value
print('expression')         # a function call


# 5. STATEMENTS

# "A unit of code that the Python interpreter can execute"
# Statements can contain expressions.

"""
uniqname = arwhyte          # variable assignment statement
if x < y:                   # if statement containing the expression x < y
import json                 # import statement (accessing modules)
return value                # return statement (ends execution of a function call)
"""

# 6. STRING LITERAL FORMATTING

# Quotes and Apostrophes
line = "Hail! to the conqu'ring heroes"  # apostrophe surrounded by double quotes

# Multi-line string (apostrophe surrounded by triple quotes)
# Note: triple single quotes also works in this example
chorus = """Hail! to the victors valiant
Hail! to the conqu'ring heroes
Hail! Hail! to Michigan
the leaders and best"""

# Escape characters
# Commence with back slash (\)

line = 'Hail! to the conqu\'ring heroes' # escape the apostrophe

# Line break (\n)s
print('Hail! to the victors valiant\nHail! to the conqu\'ring heroes\n')

# Raw string (prefix string with letter 'r')
raw_line = r"Hail! to the victors valiant\nHail! to the conqu\'ring heroes\n"
print(raw_line)


# 7. STRING METHODS
# String: immutable sequence of characters commonly used to represent text.
# A string object (instance) is provisioned with a number of string methods that
# can be used to perform operations on the string and return a new value.
# See https://www.w3schools.com/python/python_ref_string.asp.

line = 'Hail! Hail! to Michigan'

# A few examples

# Convert string to lower case
lower_case = line.lower()
print(lower_case)

# Convert string to upper case
upper_case = line.upper()
print(upper_case)

# Boolean checks
print(lower_case.islower())
print(upper_case.isupper())

# Replace a target value with another
huzzah = line.replace('Hail', 'Huzzah')
print(huzzah)

# Remove leading/trailing characters (also str.lstrip() and str.rstrip())
leaders = '    leaders and the best    '
strip = leaders.strip()
print(strip)

leaders = '@#&$^    leaders and the best    @#&$^'
strip = leaders.strip('@#&$^')
print(strip)

# Concantenate strings by passing one through another
join = ' '.join(line)
print(join)

# Gotcha: str.join() takes one value only so a list is required to join string values
join = ''.join([line, 'leaders and the best'])
print(join)

# Split string at specified delimiter and return a list
split = line.split()
print(split)

# Split string on a specified delimiter
spam = 'Spam, Spam, Spam'
split = spam.split(', ') # note trailing white space
print(split)

# Split lines at line breaks and return a list
splitlines = chorus.splitlines()
print(splitlines)

# String length (use built-in len() function)
char_count = len(line) # return number of characters
print(char_count)

word_count = len(line.split()) # split on white space
print(word_count)

line_count = len(splitlines) # return number of elements in list
print(line_count)


# 8. STRING CONCATENATION/FORMATTING (variations on a theme)

course_number = 'SI 506'
print(course_number)
course_name = 'Introduction to Programming'
print(course_name)
semester = '2020 Winter'
print(semester)

# example string: SI 506: Introduction to Programming (2020 Winter)

# Plus (+) operator
course_title = course_number + ': ' + course_name + ' (' + semester + ')'
print(course_title)

# Percent (%) placeholder (ye olde way -- not recommended)
# Note. % also serves as the modulus operator (discuss in more detail later)
course_title = "%s: %s (%s)" % (course_number, course_name, semester)
print(course_title)

# str.format() method (better)
course_title = "{}: {} ({})".format(course_number, course_name, semester)
print(course_title)

# Formatted string literal a.k.a f-string (Python 3.6+)
# readable, less verbose -- recommended
course_title = f"{course_number}: {course_name} ({semester})"
print(course_title)


# 9. ASSIGN STRINGS TO A LIST

# A list is a sequence of elements, akin to an array.

# An empty list
instructors = []

# A list of strings
instructors = ['Anthony', 'Andrew', 'Max', 'Morgan']
print(f"instructors = {instructors}")

# Another list of strings
assistants = ['Shrijesh', 'Thomas']
print(f"assistants = {assistants}")

# Concatenate two lists with plus (+) operator
teaching_team = instructors + assistants
print(f"teaching_team = {teaching_team}")

# Append an element to a list
teaching_team = ['Anthony', 'Andrew', 'Max', 'Morgan']
teaching_team.append('Shrijesh')
teaching_team.append('Thomas')
print(f"teaching_team = {teaching_team}")

# Extend a list with a second list
teaching_team = ['Anthony', 'Andrew', 'Max', 'Morgan']
teaching_team.extend(assistants) # add assistants
print(f"teaching_team = {teaching_team}")

# Accessing a list element
instructor_name = teaching_team[0] # zero-based index
print(f"instructor_name = {instructor_name}")
