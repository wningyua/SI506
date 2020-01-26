import string

# MONTY PYTHON'S FLYING CIRCUS SPAM SKETCH MENU (1970)

# Background, video (absurdist comedy)
# https://en.wikipedia.org/wiki/Spam_(Monty_Python)
# https://www.dailymotion.com/video/x9fly1

# Objectives
# 1. Work with sequences (multi-line strings and simple lists)
# 2. Perform operations on a "source" string without modifying it (best practice)
# 3. Reassign variables
# 4. Utilize string and list methods
# 5. Count characters, lines, and words
# 6. Use the built-in functions print(), len(), str() and type()
# 7. Encounter various string formatting operations
# 8. Insert line breaks with newline escape character ('\n')

# String and list methods (handy reference)
# String methods: https://www.w3schools.com/python/python_ref_string.asp
# List methods: https://www.w3schools.com/python/python_ref_list.asp


# 1.0 SPAM SKETCH MENU
menu = """Egg and bacon
Egg, sausage and bacon
Egg and Spam
Egg, bacon and Spam
Egg, bacon, sausage and Spam
Spam, bacon, sausage and Spam
Spam, egg, Spam, Spam, bacon and Spam
Spam, Spam, Spam, egg and Spam
Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam
Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top, and Spam"""

print('\nmenu = ' + menu + '\n') # string concatenation with newline escape character
menu_type = type(menu)
print('object type = ' + str(menu_type) + '\n') # cast type to string

# 2.0 STRING METHODS

# Check if "Spam" is the first word
is_first_word_spam = menu.startswith("Spam")
print(f"is_first_word_spam = {is_first_word_spam}\n")

# Check if "Spam" is the last word
is_last_word_spam = menu.endswith("Spam")
print(f"is_last_word_spam = {is_last_word_spam}\n")

# Switch menu text to lower case
lower_case_menu = menu.lower()
print("lower_case = %s\n" % lower_case_menu) # old school placeholder formatting

# Switch only "Spam" to lower case
spam_menu = menu.replace('Spam', 'spam')
print("spam_menu = {}\n".format(spam_menu)) # str.format()

# Return character count
char_count = len(menu) # built-in function
print("char_count = {}\n".format(char_count))

# Return line count
line_count = len(menu.splitlines())# splits on line break
print("line_count = %s\n" % line_count)

# Return list of "words" (punctuation retained)
words = menu.split() # returns list
print("words = {}\n".format(words)) # str.format()

# Drop commas then return word list
words = menu.replace(',', '')   # method chaining
print("words = {}\n".format(words))

# Method chaining order matters
# words = menu.split().replace(',', '') # AttributeError list.replace() doesn't exist
# print(f"words = {words}\n")

# Return word count
word_count = len(words)
print(f"word_count = {word_count}\n") # formatted string literal (f-string)

# Return "Spam" count
spam_count = menu.count('Spam')
print(f"spam_count = {spam_count}\n")

# Replace Spam with Tofu
tofu_menu = menu.replace('Spam', 'Tofu')
print(f"tofu_menu = {tofu_menu}\n")

# Add trailing " + Spam" and newline ('\n') to each line
tofu_spam_menu = ' + Spam\n'.join(menu.splitlines())  # str.join()
print(f"tofu_spam_menu = {tofu_spam_menu}\n")

# Split lines and return a list (original menu)
lines = menu.splitlines()

# Return first line by its index position
first_line = lines[0] # zero-based index
print(f"first_line = {first_line}\n")

last_line = lines[-1] # negative index; more on this next week
print(f"last_line = {last_line}\n")


# 3.0 LIST METHODS

# Use list assigned to lines variable (see above)
#lines = [] # WARN: comment out once lines variable is assigned list above.

# Append 'Red beans and rice + Spam' to list (in-place)
# lines.? # modify in-place before variable reassignment
lines.append('Red beans and rice + Spam')
print(f"new menu = {lines}\n")

# Remove "Lobster Thermidor . . ."" menu item from list (in-place)
# lines.?
lines.remove('Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top, and Spam')
print(f"No Lobster Thermidor = {lines}\n")

# Return index position by value
# Get index position: 'Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam'
index = lines.index('Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam')
print(f"index postion = {index}\n")

# Return element removed ("popped") from list using index variable value
menu_item = lines.pop(index) # returns popped element before removal
print(f"menu item = {menu_item}\n")

# Extend list with another list (in-place)
menu_items = ['Cereal and Yogurt + Spam', 'Eggs, Hash browns, fruit plate + Spam']
lines.extend(menu_items)
print(f"new menu extended = {lines}\n")

# Insert element at index position "1" (in-place)
oatmeal = 'Oatmeal, fruit plate, + Spam'
lines.insert(1, 'Oatmeal, fruit plate, + Spam')
print(f"Oatmeal added to the menu = {lines}\n")

# Sort the list (in-place)
lines.sort() # default alpha sort
print(f"new menu sorted = {lines}\n")


# 4.0 BONUS (Out of scope for SI 506)

# Remove all punctuation using str.translate() & string.punctuation constant
# https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string

finis = """The End"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
finis = finis.translate(finis.maketrans('', '', string.punctuation))
print(f"{finis}\n")
