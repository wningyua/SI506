# Lecture 09_01 Exercise Objectives

# 01. Read a function's Docstring
# 02. Implement counter in a function
# 03. Use range() to generate a sequence of numbers
# 04. use while loop to iterate over list
# 05. Write for loops and conditional statements to filter data
# 06. Write expressions using a membership operator (in, not in)
# 07. Call a function from another function
# 08. Control execution path from main() function


def count_musicians_range(musicians, instrument=None):
    """Return a count of musicians by their chosen instrument.
    If no instrument is provided by the caller then count all
    musicians. If an instrument is provided (e.g., 'trumpet')
    count only musicians whose instrument matches the passed in
    instrument, permitting case-insensitive matches.

    Parameters:
        musicians (list): list of musicians and their instruments
        instrument (string): filter string

    Return:
        list: filtered list of musicians and their instruments
    """

    if not instrument: # truth value
        return len(musicians) # return immediately (no if-else)

    count = 0 # initialize count

    # Access musician by index position
    for i in range(0, len(musicians)):
        musician = musicians[i].split(', ')[1].lower()
        if instrument.lower() in musician:
        # if instrument.lower() == musician: # too restrictive
            count += 1 # MUST INCREMENT
        i += 1 # MUST INCREMENT

    return count


def count_musicians(musicians, instrument=None):
    """Return a count of musicians by their chosen instrument.
    If no instrument is provided by the caller then count all
    musicians. If an instrument is provided (e.g., 'trumpet')
    count only musicians whose instrument matches the passed in
    instrument, permitting case-insensitive matches.

    Parameters:
        musicians (list): list of musicians and their instruments
        instrument (string): filter string

    Return:
        list: filtered list of musicians and their instruments
    """

    if not instrument: # truth value
        return len(musicians) # return immediately (no if-else)

    count = 0 # initialize count
    for musician in musicians:
        if instrument.lower() in musician.split(', ')[1].lower():
        # if instrument.lower() == musician.split(', ')[1].lower(): # too restrictive
            count += 1 #increment
            # count = count + 1

    return count


def is_member(musicians, musician_name):
    """Return true if named musician is in musician list;
    otherwise return false.

    Parameters:
        musicians (list): list of musicians and their instruments
        musician_name (str): musician name

    Returns:
        bool: True if match is made; otherwise False.

    """
    i = 0 # counter

    while i < len(musicians): # guard against infinite loop
        musician = musicians[i].split(', ')[0].lower()
        if musician_name.lower() == musician:
            return True # preferable to break statement
        i += 1 # MUST INCREMENT

    return False


def main():
    """Entry point for program.

    Parameters:
        None

    Returns:
        None
    """

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

    print('\n') # padding


# 1.0 COUNTER PATTERN

    # Initialize count variable in function
    # increment value in loop
    # return sum

    # Count all musicians (default)
    musician_count = count_musicians(jazz_orchestra)

    print(f"Musicians count = {musician_count}\n")

    # Count trumpeters (pass filter value)
    trumpeter_count = count_musicians(jazz_orchestra, 'trumpet')

    print(f"Trumpeter count = {trumpeter_count}\n")

    # Count saxiphonists (pass filter value)
    saxophonist_count = count_musicians(jazz_orchestra, 'saxophone')

    print(f"Saxophone count = {saxophonist_count}\n")



    # 1.0 WHILE LOOP

    # Executes statement(s) while condition remains TRUE
    # WARN: handle with care otherwise you can trigger an infinite loop
    # See https://www.w3schools.com/python/python_while_loops.asp

    # Function call outside print() statement
    musician = 'Ali Jackson'

    # UNCOMMENT
    if is_member(jazz_orchestra, musician): # truth value test
        print(f"{musician} is a member of the JLCO\n")
    else:
        print(f"{musician} is not a member of the JLCO\n")

    # Check if musician is member of the JLCO
    musician = 'Carlos Henriquez'

    # Function call embedded in print() statement
    # Eliminate if-else blocks: otherwise no impact on function call
    print(f"{musician} JLCO member: {is_member(jazz_orchestra, musician)}\n")


    # 2.0 RANGE() FUNCTION

    # Returns sequence of numbers, starting from 0 (by default),
    # increments by 1 (by default), and ends at a specified number.
    # See https://www.w3schools.com/python/ref_func_range.asp

    # UNCOMMENT First 3 musicians
    for i in range(0, 3): # mimics list slicing
         print(jazz_orchestra[i])

    print('\n') # padding

    # UNCOMMENT Last 3 musicians
    musician_count = len(jazz_orchestra)
    for i in range(musician_count - 3, musician_count):
         print(jazz_orchestra[i])

    print('\n') # padding

    # UNCOMMENT Every other musician (optional step value)
    for i in range(0, len(jazz_orchestra), 2):
         print(jazz_orchestra[i])

    print('\n') # padding

    # Count trumpeters (call function employing range())
    trumpeter_count = count_musicians_range(jazz_orchestra, 'trumpet')

    print(f"Trumpeter count using range() = {trumpeter_count}\n")

if __name__ == '__main__':
    main()
