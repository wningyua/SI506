# Lecture 08 Objectives

# 01. Access list elements by their index position
# 02. Use for loop to iterate over list
# 03. Filter lists using conditional statements
# 04. Implement the accumulator pattern
# 05. Use continue and break control statements
# 06. Create a list of lists (nested list)
# 07. Slice lists using slice notation
# 08. Implement nested for loop
# 09. Write expressions using a comparison operator (==, !=, etc.)
# 10. Write expressions using a membership operator (in, not in)
# 11. Write expressions using a logical operator (and, or, not)


# 1.0 INDEXING LISTS

# Marsalis family of Jazz musicians
marsalis_family = [
    'Ellis Marsalis, piano, teacher',
    'Branford Marsalis, saxophone, composer, band leader',
    'Wynton Marsalis, trumpet, composer, teacher, band leader, artistic director (Jazz at Lincoln Center)',
    'Ellis Marsalis III, poet, photographer, computer networking specialist',
    'Delfeayo Marsalis, trombone, producer',
    'Mboya Kenyatta Marsalis',
    'Jason Marsalis, drums, vibraphone, band leader'
    ]

print('\n') # padding

# Return first musician (Ellis, patriarch)
musician = marsalis_family[0] # index operator

print(f"First Marsalis musician = {musician}\n")

# Return last musician (negative index)
musician = marsalis_family[-1]

print(f"Last Marsalis musician = {musician}\n")

# Return Wynton Marsalis
musician = marsalis_family[2]

print(f"Wynton Marsalis = {musician}\n")

# Modify Ellis Marsalis record (father)
marsalis_family[0] = marsalis_family[0] + ', patriarch'

print(f"Ellis Marsalis = {marsalis_family[0]}\n")

# Review: add Dolores Marsalis (mother)
dolores = 'Dolores Marsalis, matriarch'
marsalis_family.append(dolores)

print(f"Marsalis List members = {marsalis_family}\n")


# RAISE EXCEPTION (UNCOMMENT)
# IndexError: list index out of range
# # print(f"Dolores Marsalis = {marsalis_family[8]}")


# 2.0 FOR LOOP

# UNCOMMENT
for member in marsalis_family:
    print(member)


# 2.1 FOR LOOPS AND CONDITIONAL STATEMENTS (FILTERING)

# Accumulator pattern (populate empty list with filter results)
# Return teachers (name only)
teachers = [] # accumulator variable assignment

for member in marsalis_family:
    if 'teacher' in member.lower(): # membership operator
        full_name = member.split(', ')[0]
        teachers.append(full_name)

print(f"Marsalis teachers = {teachers}\n")


# Accumulator pattern (populate empty list with filter results)
# Return members not listed as composers (name only)
non_composers = [] # accumulator variable assignment

for member in marsalis_family:
    if 'composer' not in member.lower(): # membership operator
        full_name = member.split(', ')[0] # index operator
        non_composers.append(full_name)

print(f"Marsalis non-composers = {non_composers}\n")


# Return members who are either composers or producers (name only)
composer_producers = [] # accumulator variable assignment

for member in marsalis_family:
    if 'composer' in member.lower() or 'producer' in member.lower():
        full_name = member.split(', ')[0] # index operator
        composer_producers.append(full_name)

print(f"Marsalis composers or producers = {composer_producers}\n")


# 2.2 CONTROL FLOW: CONTINUE AND BREAK STATEMENTS

# 2.2.1 CONTINUE STATEMENT
# continue: proceed to next loop iteration

# Return musicians only (if-elif-else continue)
marsalis_musicians = [] # accumulator variable assignment

for member in marsalis_family:
    if 'piano' in member.lower():
        marsalis_musicians.append(member)
    elif 'saxophone' in member.lower():
        marsalis_musicians.append(member)
    elif 'trumpet' in member.lower():
        marsalis_musicians.append(member)
    elif 'trombone' in member.lower():
        marsalis_musicians.append(member)
    elif 'drums' in member.lower():
        marsalis_musicians.append(member)
    else:
        continue # proceed to next loop iteration

print(f"Marsalis musicians 01 = {marsalis_musicians}\n")


# Avoiding use of continue
# Return musicians only (nested for loop)
marsalis_musicians = [] # accumulator variable assignment
instruments = ['drums', 'piano', 'saxophone', 'trombone', 'trumpet', 'vibraphone']

for member in marsalis_family:
    for instrument in instruments:
        if instrument in member.lower(): # necessary but not sufficient
            marsalis_musicians.append(member)

# Bad: duplicate record appended
#print(f"Marsalis musicians 02 = {marsalis_musicians}\n")


# Return musicians only (nested for loop)
marsalis_musicians = [] # accumulator variable assignment
instruments = ['drums', 'piano', 'saxophone', 'trombone', 'trumpet', 'vibraphone']

for member in marsalis_family:
    for instrument in instruments:
        if member not in marsalis_musicians and instrument in member.lower(): # Good
            marsalis_musicians.append(member)

# Good: duplicate record avoided
# print(f"Marsalis musicians 03 = {marsalis_musicians}\n")


# 2.2.1 BREAK STATEMENT
# break: terminate loop and exit block

# Return first trumpeter found in list (break)
for member in marsalis_family:
    if 'trumpet' in member.lower():
        trumpeter = member.split(', ')[0] # index operator
        print(f"Marsalis Trumpeter = {trumpeter}\n")
        break # terminate loop
    # break # <-- UNCOMMENT: indention matters; terminates loop prematurely


# Avoiding use of break (write a function!)
def get_musicians_by_instrument(people, instrument):
    musicians = []
    for person in people:
        if instrument.lower() in person.lower():
            musicians.append(member.split(', ')[0]) # index operator)
    return musicians


# Call function
trumpeter = get_musicians_by_instrument(marsalis_family, 'trumpet')

# Print first trumpter encountered in list
print(f"Marsalis Trumpeter 2 = {trumpeter[0]}\n")


# 3.0 LIST SLICING
# Working with subsets of parent list

# Jazz at Lincoln Center Orchestra (JLCO)
jazz_orchestra = [
    'Wynton Marsalis, trumpet',
    'Walter Blanding, saxophone',
    'Chris Crenshaw, trombone',
    'Vincent Gardner, trombone',
    'Victor Goines, saxophone',
    'Carlos Henriquez, bass',
    'Sherman Irby, alto saxophone',
    'Elliot Mason, trombone',
    'Ted Nash, saxophone',
    'Paul Nedzela, baritone saxophone',
    'Dan Nimmer, piano',
    'Marcus Printup, trumpet',
    'Kenny Rampton, trumpet'
]

# Return first three musicians
musicians = jazz_orchestra[:4]

print(f"First 3 musicians = {musicians}\n")

# Return last three musicians (negative slicing)
musicians = jazz_orchestra[-3:]

print(f"Last 3 musicians = {musicians}\n")

# Return 2nd - 6th musicians in jazz_musicians
musicians = jazz_orchestra[1:6]

print(f"2nd - 6th musicians = {musicians}\n")

# Return 6th - 9th musicians in jazz_musicians (negative slicing)
musicians = jazz_orchestra[-8:-4]

print(f"6th - 9th musicians = {musicians}\n")

# Loop over list slice
# Drop first two and last two musicians
musician_subset = []
for musician in jazz_orchestra[2:11]:
    musician_subset.append(musician)

print(f"3rd - 10th musicians = {musician_subset}\n")


# 5.0 NESTED LISTS

# Return a list of lists
jazz_musicians = []

for jazz_musician in jazz_orchestra:
    musician = jazz_musician.split(', ')
    jazz_musicians.append(musician)

print(f"Jazz Musicians = {jazz_musicians}\n")


# Return list of instruments
instruments = []

for jazz_musician in jazz_orchestra:
    instrument = jazz_musician.split(', ')[1] # index operator
    instruments.append(instrument)

print(f"Jazz Orchestra Instruments = {instruments}\n")


# Return a unique list of instruments and then sort
instruments = []

for jazz_musician in jazz_orchestra:
    instrument = jazz_musician.split(', ')[1] # index operator
    if instrument not in instruments: # membership operator
        instruments.append(instrument)

instruments.sort() # call in-place sort method
print(f"Jazz Orchestra Instruments = {instruments}\n")


# Return list of saxophone instrument types (multiple slicing)
saxophones = instruments[:2] + instruments[4:5] # concatenate two lists


# Return a list of saxophonists (in operator)
saxophonists = []
instrument = 'saxophone'

for jazz_musician in jazz_orchestra:
    if instrument in jazz_musician.split(', ')[1].lower(): # == comparison operator too restrictive
        saxophonists.append(jazz_musician)

print(f"Jazz Orchestra Saxiphonists 02 = {saxophonists}\n")


# Return a list of saxophonists (nested loop)
saxophonists.clear() # removes elements

for jazz_musician in jazz_orchestra:
    for sax in saxophones:
        if sax == jazz_musician.split(', ')[1].lower(): # warn: membership operator in creates dups
            saxophonists.append(jazz_musician)

print(f"Jazz Orchestra Saxiphonists 01 = {saxophonists}\n")
