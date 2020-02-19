# Lecture 12 Objectives

# 01. Understand the differences between a tuple and a list.
# 02. Familiarize yourself with a tuple's syntax
# 03. Pack and unpack a tuple (assignment)
# 04. Concatenate and multiply tuples
# 05. Use built-in functions with tuples
# 06. Return a tuple of items as a function return value
# 07. Recognize that dictionary.items() return tuples
# 08. Employ a tuple as a dictionary composite key


# 1.0 LIST (MUTABLE)

jamaica = ['Jamaica', 'JAM', 'Kingston']

print(f"\n{jamaica} = {type(jamaica)}\n")


iso_alpha3_code = jamaica[1] # index operator

print(f"Jamaica ISO alpha code = {iso_alpha3_code}\n")


jamaica = jamaica[:2] # slice out capital

jamaica.append(1962) # mutable (year of independence)

jamaica[-1] = '6 August 1962' # mutable (add day and month)


# Just for fun: pad last print() with newline character
# Iterate over range() set to length of jamaica list
jamaica_size = len(jamaica)
for i in range(jamaica_size):
    if i < jamaica_size - 1:
        print(jamaica[i])
    else:
        print(f"{jamaica[i]}\n") # pad last line



# 1.1 TUPLE (IMMUTABLE)

# Ordered sequence of items
# Immutable (once created it cannot be changed)
# Items accessible via indexing and slicing
# Accessing tuple items usually faster than accessing list elements (optimize)
# Comparable (e.g., tuple A < tuple B)
# Hashable (can be used as composite keys in dictionary)
# Enclose with parentheses (convention, not strictly required)

jamaica = ('Jamaica', 'JAM', 'Kingston') # (...) for easy identification
jamaica = 'Jamaica', 'JAM', 'Kingston' # legal (tuple packing)

print(f"{jamaica} = {type(jamaica)}\n")


capital = jamaica[-1] # index operator

print(f"Jamaican capital = {capital}\n")


jamaica = jamaica[:2] # slice

print(f"Jamaica slice = {jamaica}\n")


# UNCOMMENT
# Exception raised: TypeError: 'tuple' object does not support item assignment
# jamaica[-1] = '6 August 1962' # immutable


# Built-in enumerate() function (very cool)
# Takes an iterable (e.g., list, tuple) and for each element/item returns
# a tuple comprising the item's index value and the item itself.

jamaica_enumerated = list(enumerate(jamaica)) # list of tuples (cool)

print(f"jamaica_enumerated = {jamaica_enumerated}\n")


# Just for fun: pad last print() with newline character using enumerate()

# another for loop" using enumerate()

jamaica_len = len(jamaica)

for i, item in enumerate(jamaica):
    if i < jamaica_len - 1:
        print(f"{i} {item}")
    else:
        print(f"{i} {item}\n") # pad last line



# 2.0 SINGLE ITEM TUPLE

# Trailing comma is required, else interepreted as the item data type.

jerk_pit = ('Jamaican Jerk Pit',) # trailing comma
five_oh_six = (506,) # trailing comma

print(f"jerk_pit type = {type(jerk_pit)}\n")
print(f"five_oh_six = {type(five_oh_six)}\n")


jerk_pit = ('Jamaican Jerk Pit') # a string
five_oh_six = (506) # an int

print(f"jerk_pit type = {type(jerk_pit)}\n")
print(f"five_oh_six = {type(five_oh_six)}\n")



# 3.0 TUPLE ASSIGNMENT (PACKING/UNPACKING)

jamaica = ('Jamaica', 'JAM', 'Kingston') # tuple packing


country_name, iso_alpha3_code, capital = jamaica # tuple unpacking

print(f"country_name = {country_name}\n")


# BEWARE: Number of variables on left must equal the number of variables on the
# right of the assignment operator (=) otherwise a ValueError will be triggered.

# UNCOMMENT
# ValueError: too many values to unpack (expected 2)
# country_name, iso_alpha3_code = jamaica # raises exception



## 4.0 CONCATENATE TUPLES

# Use the plus (+) operator to concatenate tuples in order to create a new tuple.

economy = ('Developing', 'Upper middle income')

jamaica_economy = jamaica + economy

print(f"jamaica_economy = {jamaica_economy}\n")



## 5.0 MULTIPLY TUPLES

nums = (0, 1) * 5

print (f"{nums}\n")



## 6.0 COMPARE TUPLES

# Python compares the first item from each sequence for equality. If equal
# the second item from each sequence is compared, and so on until a pair is
# located that differs.

expression = False

if (0, 1, 2) < (2, 3, 4):
    expression = True

print(f"{expression}\n")

expression = False

if (0, 5, 10) < (0, 4, 9):
    expression = True

print(f"{expression}\n")



# 7.0 BUILT-IN FUNCTIONS AND TUPLES

# Fibonacci sequence: starting from 0 and 1, succeeding numbers represent the
# sum of the two preceding numbers

fib = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144) # truncated

fib_len, fib_min, fib_max = len(fib), min(fib), max(fib) # unpacking

print(f"fib_len = {fib_len}, fib_min = {fib_min}, fib_max = {fib_max}\n")



# 8.0 FUNCTION RETURN VALUE AND TUPLES

# Functions are limited to returning a single value. But the single value
# to be returned can take the form of a tuple containing multiple items.
# Consider using a tuple when you need to return data that forms a
# natural association as in the example below.

def get_bob_sleigh_team(teams, year):
    for team in teams:
        if team[0] == year:
            return team[1], team[2] # a tuple
            # return team[1:] # tuple slice
        else:
            continue


# Jamaican two-person Bobsleigh teams (Winter Games, pilot, breakman)
jamaican_bobsleigh_teams = [
    (1988,'Dudley Stokes','Michael White'),
    (1992,'Devon Harris','Ricky McIntosh'),
    (1994,'Dudley Stokes','Wayne Thomas'),
    (1998,'Devon Harris', 'Michael Morgan'),
    (2002,'Winston Watts','Lascelles Brown'),
    (2014,'Winston Watts','Marvin Dixon'),
    (2018,'Jazmine Fenlator-Victorian','Carrie Russell')
]

team = get_bob_sleigh_team(jamaican_bobsleigh_teams, 2018)

print(f"2018 team = {team}\n")


pilot, brakeman = team # unpack

print(f"pilot = {pilot}, brakeman = {brakeman}\n")



# 9.0 DICTIONARY ITEMS AND TUPLES

country = {
    'name': 'Jamaica',
    'alpha3_code': 'JAM',
    'capital': 'Kingston',
    'independence_year': 1962
}

country_items = list(country.items()) # convert dict_items object to list

print(f"country_items = {country_items}\n") # list of tuples



# 10.0 DICTIONARY COMPOSITE KEYS (HASH)

# Unlike lists, tuples are immutable and therefore hashable,
# which means that a tuple can be used as a dictionary key.

# Two-man teams (yes, even women's teams are termed 'two-man')
olympic_bobsleigh = {}

olympic_bobsleigh[2014, 'Canada', 'women'] = 'Kaillie Humphries','Heather Moyse'
olympic_bobsleigh[2014, 'USA', 'women'] = 'Elana Meyers', 'Lauryn Williams'
olympic_bobsleigh[2014, 'USA', 'women'] = 'Jamie Greubel', 'Aja Evans'
olympic_bobsleigh[2014, 'Switzerland', 'men'] = 'Beat Hefti', 'Alex Baumann'
olympic_bobsleigh[2014, 'USA', 'men'] = 'Steven Holcomb', 'Steven Langton'
olympic_bobsleigh[2014, 'Latvia', 'men'] = 'Oskars Melbārdis', 'Daumants Dreiskens'
olympic_bobsleigh[2018, 'Canada', 'women'] = 'Kaillie Humphries','Phylicia George'
olympic_bobsleigh[2018, 'Canada', 'men'] = 'Justin Kripps','Alexander Kopacz'
olympic_bobsleigh[2018, 'Germany', 'women'] = 'Mariama Jamanka','Lisa Buckwitz'
olympic_bobsleigh[2018, 'Germany', 'men'] = 'Francesco Friedrich','Thorsten Margis'
olympic_bobsleigh[2018, 'Jamaica', 'women'] = 'Jazmine Fenlator-Victorian','Carrie Russell'
olympic_bobsleigh[2018, 'Latvia', 'men'] = 'Oskars Melbārdis','Jānis Strenga'
olympic_bobsleigh[2018, 'USA', 'women'] = 'Elana Meyers Taylor','Lauren Gibbs'


for key in olympic_bobsleigh.keys():
    if key == (2018, 'Jamaica', 'women'):
        print(f"{olympic_bobsleigh[key]}\n")
        break
    else:
        continue


for key, val in olympic_bobsleigh.items():
    if key[1:] == ('Canada', 'women'): # tuple slice
        print(val)
    else:
        continue

print('\n') # padding
