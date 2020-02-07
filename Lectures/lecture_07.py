# Lecture 07 Exercise Objectives

# 01. Implement a search engine (toy)
# 02. Utilize main() function to control execution
# 03. Write a set of utility functions
# 04. Learn how use the built-in input() function
# 05. Access list elements by their index position
# 06. Employ nested conditional statements
# 07. Perform truth value tests on objects
# 08. Write expressions using a membership operator (in, not in)
# 09. Read a function's Docstring
# 10. Understand why we employ the pass keyword
# 11. Begin to discern patterns
# 12. BONUS: Get to know the for loop (list iteration)


def placeholder():
    """ pass keyword is considered a null operation.
    When executed nothing happens. Used as a placeholder
    when building out functions or classes.
    """
    pass # null operation


def count_records(records):
    """Count list elements.

    Parameters:
        records (list): records to be counted

    Returns:
        int: count of records
    """
    return len(records)


def find_records(dataset, search_string):
    """Retrieve records filtered on search string.

    Parameters:
        dataset (list): dataset to be searched
        search_string (str): query string

    Returns:
        list: filtered list of records
    """
    records = [] # empty list (accumulator pattern)
    for record in dataset:
        # TODO FILTER RECORDS
         if search_string.lower() in record.lower(): # case insensitive
            records.append(record) # INDENT

    return records


def get_course_number(record, delimiter=','):
    """Spit string and return course number by index position.

    Parameters:
        record (str): string to be split
        delimiter (str): delimiter used to perform split

    Returns:
        str: course number
    """
    return record.split(delimiter)[0]


def get_person_name(record, delimiter=','):
    """Spit string and return name by index position.

    Parameters:
        record (str): string to be split
        delimiter (str): delimiter used to perform split

    Returns:
        str: person name
    """
    return record.split(delimiter)[1]


def get_person_role(record, delimiter=','):
    """Spilt string and return role by index position.

    Parameters:
        record (str): string to be split
        delimiter (str): delimiter used to perform split

    Returns:
        str: role
    """
    return record.split(delimiter)[3]


def get_person_uniqname(record, delimiter=','):
    """Spilt string and return uniqname by index position.

    Parameters:
        record (str): string to be split
        delimiter (str): delimiter used to perform split

    Returns:
        str: uniqname
    """
    return record.split(delimiter)[2]


def calculate_percent(numerator, denominator):
    """Return percentage value, round to 2 digits precision.

    Parameters:
        numerator (int): parts of the whole
        denominator (str): the whole

    Returns:
        float: percentage value rounded (00.00)
    """
    percent = (numerator / denominator) * 100
    return round(percent, 2)


def main():
    """Entry point for program. Accepts user provided search
    string via built-in input() function. Attempts to filter
    list dataset and then print to screen string representations
    of list elements that contain the search string value along
    with base statistics. If the submitted search string is empty
    the operation is terminated and the user is invited to submit
    a search string.

    Parameters:
        None

    Returns:
        None
    """

    dataset = [
        'SI 506, Anthony Whyte, arwhyte, Instructor',
        'SI 506, Morgan Durow, mdurow, GSI',
        'SI 506, Andrew Vande Guchte, avandegu, GSI',
        'SI 506, Max Zhang, maxzhang, GSI',
        'SI 506, Thomas Krouse, tkrouse, IA',
        'SI 506, Shrijesh Siwakoti, shrijesh, IA'
        ]

    dataset_count = len(dataset) # total records

    # Prompt user for input.
    search_string = input('\nPlease enter search string: ')

    if search_string: # truth value test (i.e., not empty)

        # Find records
        records = find_records(dataset, search_string)

        if records: # truth value test (i.e., not empty)
            # Get count
            record_count = count_records(records)
            print(f"\nTotal records: {dataset_count}\n") # padding

            hits_percent = calculate_percent(record_count, dataset_count)
            print(f"Records returned: {record_count} ({hits_percent}%)\n")

            # Loop over records (iterate) and print each record
            for record in records:
                course_number = get_course_number(record, ', ')
                name = get_person_name(record, ', ')
                uniqname = get_person_uniqname(record, ', ')
                role = get_person_role(record, ', ')

                print(f"{course_number}: {name}, {uniqname}, {role}")

            print('\n') # padding
        else:
            print(f"No records found.\n")
    else:
        print(f"\nEmpty search string submitted. Please try again.\n")

# Python renames file executed from the command line to '__main__'s
if __name__ == '__main__':
    main()