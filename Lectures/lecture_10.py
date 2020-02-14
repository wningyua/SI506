# Lecture 10 Objectives

# 01. Understand limitations of the list data type
# 02. Learn the value of the dictionary data structure
# 03. Add, assign, modify, delete key/value pairs
# 04. Iterate over keys, values
# 05. Loop over dictionary items

# 1.0 LIMITATIONS OF THE LIST

# Example: express Wynton Marsalis bio sketch using lists
# Data source: 'https://en.wikipedia.org/wiki/Wynton_Marsalis'

# Note use of nested lists
musician = [
    'Wynton Learson Marsalis',
    'October 18, 1961',
    58,
    'New Orleans, Louisiana, USA',
    ['Jazz','Classical','Dixieland'],
    ['Musician','Composer','Educator','Artistic Director'],
    ['Trumpet'],
    'active'
    ]

print(f"\nmusician = {musician}\n")

# Get full name
full_name = musician[0]

print(f"full name = {full_name}\n")

# Get last name
last_name = musician[0].split()[-1] # default is split by space

print(f"last name = {last_name}\n")

# Get state born in
state = musician[3].split(", ")[1]

print(f"born in = {state}\n")

# Get 1st listed genre
primary_genre = musician[4][0] # chained index operaters

print(f"primary genre = {primary_genre}\n")

# Get two most recent roles
newest_roles = musician[-3][-2:]

print(f"newest_roles = {newest_roles}\n")

# Observations
# 1. Data is not labeled.
# 2. Knowing what the data represents requires "external" knowledge.
# 3. Embedding hints (i.e., musician[2] represents the musician's age)
#    complicates the data structure.
# 4. Lists have their limits.

musician[2] = 'age 58' # yuck
age = musician[2][-2:] # string slicing (note: false positive linting)

print(f"age = {age}\n")


# 2.0 THE DICTIONARY

# Python dictionaries are considered associative arrays,
# wherein each value defined within the dictionary is
# associated with a key that is used to access the value.

# You'll often hear people refer to dictionaries as
# unordered sets of key-value pairs or as maps.

# However, since Python 3.7 dictionary order is guaranteed
# to be the key/value pair insertion order.

# The beauty of the dictionary is the ability to identify data
# values by a label or key, usually rendered as a readable
# string though not always (int, tuple also used as keys).
# In other words, you can embed meaning into a data structure.

# An (empty) dictionary
musician = {} # curly braces


# 1.1 ADDING KEY/VALUE PAIRS TO A DICTIONARY

# Assign key/value pairs
musician['first_name'] = 'Wynton'
musician['middle_name'] = 'L.'
musician['last_name'] = 'Marsalis'
musician['birth_date'] = 'October 18, 1961'
musician['age'] = 58

# Alternative: create dictionary with built-in dict() function (relative slow)
musician = dict(
    first_name = 'Wynton',
    middle_name = 'L.',
    last_name = 'Marsalis',
    birth_date = 'October 18, 1961',
    age = 58
    )

# Alternative: define a dictionary literal (fast)
place = {
    'city': 'New Orleans',
    'state': 'Louisiana',
    'country': 'USA'
}

musician['birth_place'] = place # nested dictionary

print(f"\nmusician = {musician}\n")


# 2.0 BASIC DICTIONARY OPERATIONS

# Assign value
last_name = musician['last_name']

print(f"last_name = {last_name}\n")

# Modify value
musician['middle_name'] = 'Learson'

print(f"middle name change = {musician['middle_name']}\n")

# Delete key/value
del musician['middle_name'] # delete keyword

print(f"musician = {musician}\n")

# Add additional key/value pairs based on Wikipedia bio
musician['genres'] = [
    'Jazz',
    'Classical',
    'Dixieland'
    ]
musician['occupations'] = [
    'Musician',
    'Composer',
    'Educator',
    'Artistic Director'
    ]
musician['instruments'] = ['Trumpet'] # single element list
musician['is_active'] = True # boolean

print(f"musician = {musician}\n")


# 3.0 DICTIONARY METHODS (A SELECT LIST)
# For a complete list see
# https://www.w3schools.com/python/python_ref_dictionary.asp

# Get value by key
age = musician.get('age')

print(f"age = {age}\n")

# Get list of keys
musician_keys = musician.keys() # returns dict_keys list

print(f"musician_keys = {musician_keys}\n")

# Get list of values
musician_values = musician.values() # returns dict_keys list

print(f"musician_values = {musician_values}\n")

# Update dictionary with additional key / value pairs
# Behavior: overwrite existing value if key(s) match; else
# add new key/value pairs.
musician.update({'website': 'http://wyntonmarsalis.org/'}) # add
musician.update({'birth_date': '18 October 1961'}) # override

print(f"musician = {musician}\n")


# 4.0 LOOPING OVER A DICTIONARY

# Loop over dictionary by key
for key in musician:
    if type(musician[key]) == list:
        print(f"musician list value keys = {key}")

print('\n') # padding


# Loop over dictionary keys only (dict.keys()):
for key in musician.keys():
    if type(musician[key]) == str:
        print(f"musician str value keys = {key}")

print('\n') # padding


# Loop over dictionary values only (dict.values())
for value in musician.values():
    if type(value) == list:
        print(f"musician list values = {value}")

print('\n') # padding


# Loop over both the keys and values (dict.items())
# Example: find list key/value pairs and add to new dictionary
# Filtering items with the accumulator pattern
bio_lists = {}
for key, value in musician.items():
    if type(value) == list:
        bio_lists[key] = value

print(f"bio lists = {bio_lists}\n")


# Loop over both the keys and values (dict.items())
# Example: write unique list values to labels list
# Filtering items with the accumulator pattern
labels = []
for key, value in musician.items():
    if type(value) == list:
        for val in value:
            if type(val) == str and val.capitalize() not in labels:
                labels.append(val)

print(f"labels = {labels}\n")
