# SI 506 Lecture 03

# 1. COMMENTS

# A single line comment <-- commences with hash (#) character

"""
This is a block comment comprising a multi-line
string. This is actually a string constant that is
denoted by the use of triple quotation marks.
"""


# 2. PRINTING TO THE SCREEN

# The print() built-in function
print('Hello SI 506')


# 3 VALUES (OBJECTS)
# Immutable: once created object state is unchangeable.
# Mutable: once created object state is changeable.

'Morgan' # a string (immutable)
506 # an integer (immutable)
['SI 506', 'SI 507'] # a list (mutable)


# 4. VARIABLE NAMING

# Good

course_short_name = 'SI506'
course_list = ['SI506', 'SI507', 'SI508'] # a list []

# Bad

c = 'SI506' # opaque (unfriendly)
courseList = ['SI506', 'SI507', 'SI508'] # camelcase frowned upon

# Ugly (Interpreter will raise a SyntaxError, uncomment to confirm)

# 506_umsi = 'SI506' # no leading integers permitted
# $number = 506 # no special characters permitted (e.g., @, %, $, &, !)
# course-list = ['SI506', 'SI507', 'SI508'] # no dash permitted
# course name = 'SI506' # no whitespace permitted


# 5. VARIABLE ASSIGNMENT

# Assign a string to a variable (variable = 'value')

course_number = 'SI 506'
print(course_number)
course_name = 'Introduction to Programming'
print(course_name)
semester = '2020 Winter'
print(semester)

uniqname = 'arwhyte'
print(uniqname)
umich_domain = 'umich.edu'
print(umich_domain)

# Assign a multi-line string to a variable

chorus = """
Hail! to the victors valiant
Hail! to the conquering heroes
Hail! Hail! to Michigan
the leaders and best!
"""
print(chorus)


# 6. VARIABLE ALIASING (BEWARE)
# Variables can point to the same value.
# Behavior varies between mutable and immutable objects.

# immutable object (string)

campus_id = uniqname
print(f"campus_id = {campus_id}")

uniqname = 'csev'

print(f"uniqname = {uniqname}")
print(f"campus_id = {campus_id}")

# mutable object (list)

uniqnames = ['arwhyte', 'csev', 'nantin']
print(f"uniqnames = {uniqnames}")

campus_ids = uniqnames
print(f"campus_ids = {campus_ids}")

uniqnames[0] = 'ssciolla' # assigns first element (zero-based index) a new value
print(f"campus_ids = {campus_ids}") # list has mutated


# 7. TYPES
# Values can be distinguished by their type.
# type(<value>), a handy built-in function for determining the type of a value or expression

first_name = 'Morgan'
first_name_type = type(first_name)
print(first_name_type)


# 8. STRING CONCATENATION/FORMATTING (variations on a theme)

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

# Email address
email_address = f"{uniqname}@{umich_domain}"  # add variable references
print(email_address)


# 9. Basic arithmetic operations (addition, subtraction, multiplication, division)

# Assign an integer to a variable (variable = value)

lecturer_count = 1
gsi_count = 3
ia_count = 2
roster_count = 107
lab_section_count = 5

# Addition (+)
teaching_team_count = 1 + 3 + 2
teaching_team_count = lecturer_count + gsi_count + ia_count
print(f"teaching_team_count = {teaching_team_count}")

# Subtraction (-)
instructor_count = 6 - 2
instructor_count = teaching_team_count - ia_count
print("instructor_count = {}".format(instructor_count))

# Multiplication (*)
max_course_enrollment = 5 * 25
max_course_enrollment = lab_section_count * 25
print("max_course_enrollment = " + str(max_course_enrollment))

# Division a.k.a floating point division (/)
avg_lab_section_size = roster_count / lab_section_count # returns float data type
print("lab_section_avg_size = %s" % avg_lab_section_size)

# Floor division a.k.a integer division (//)
avg_lab_section_size = roster_count // lab_section_count
print(f"lab_section_avg_size = {avg_lab_section_size}")

# Gotchas
floor_div = 10 / 3 # floating point division
print(floor_div)
floor_div = 10 // 3 # floor division (int / int)
print(floor_div)
floor_div = 10.5 // 3 # floor division (float / int)
print(floor_div)
floor_div = 10 // 3.5 # floor division (int / float)
print(floor_div)


# 10. BONUS: ASSIGN STRINGS TO A LIST

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
