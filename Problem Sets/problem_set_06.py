# PROBLEM SET 6

# Importing some required libraries:
import csv # You'll use this one!
import operator # Don't worry about this one.

infile = "parks.csv"
outfile = "parkarea.csv"

# PROBLEM STATEMENT
#
# You have been asked to determine which US state has the largest area of national parks, given
# a CSV file ("parks.csv") that contains information on all of the national parks in the US.
# Build a python script that will create an output file ("parkarea.csv") that contains rows
# in the following format:
#
#     <state two-letter identifier>,<area of national parks in km^2 contained in that state>
#
# As an example, the output file should contain the following rows:
"""
MI,2287.16
TN,2085.96
CO,1575.536
"""
# To accomplish this task, build out the following stubbed functions. We have provided one
# function for you <sort_dictionary_by_value>. PLEASE DON'T CHANGE ANY CODE IN THIS FUNCTION,
# however, please read the docstring to understand how it works and what it is doing!


def sort_dictionary_by_value(dictionary):
    """
    DON'T CHANGE THIS FUNCTION. This function sorts a dictionary by its values in a
    descending fashion.

    Parameters:
        dictionary (dict): A dictionary to be sorted.

    Returns:
        dict: The sorted dictionary.
    """

    desc_dictionary = dict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True))

    return desc_dictionary

# BEGIN CODING HERE - - - - - - - - - - - - - - - - - - - - - - -

def read_csv_file(input_filepath):
    """
    This function reads a .csv file and parses it into a list of dictionaries,
    where each dictionary is formed from the data on one line of the .csv file.
    This function takes one argument <input_filepath>, which is the path of the file
    to be read. You will need to use the "csv" module in this function.

    The format of the returned list of dictionaries is as follows:

        [
            { <column 1 header>: <row 1 column 1 value>,
              <column 2 header>: <row 1 column 2 value>,
              <column 3 header>: <row 1 column 3 value>,
              ...etc
            },

            { <column 1 header>: <row 2 column 1 value>,
              <column 2 header>: <row 2 column 2 value>,
              <column 3 header>: <row 2 column 3 value>,
              ...etc
            },

            ...etc
        ]

    As an example, if the input file is structured as the following:

    Name,Age,Animal Type
    Lex,5,Dog
    Luke,7,Cat

    Then the returned list would be:

    [
        {
            "Name": "Lex",
            "Age": "5",
            "Animal Type": "Dog"
        },
        {
            "Name": "Luke",
            "Age": "7",
            "Animal Type": "Cat"
        }
    ]

    As a final example, if your input file was structured like so:

    Park Code,Park Name,State,Acres,Latitude,Longitude
    ACAD,Acadia National Park,ME,47390,44.35,-68.21

    Then the returned list should be:

    [
        {
            "Park Code": "ACAD",
            "Park Name": "Acadia National Park",
            "State": "ME",
            "Acres": "47390",
            "Latitude": "44.35",
            "Longitude": "-68.21"
        }
    ]

    HINT: This is the most challenging part of this problem. You may want to consider
    using nested loops with enumerate statements. Don't worry about converting any
    strings to other types here; you can handle that later.

    Parameters:
        input_filepath (str): The location of the file to read and parse.

    Returns:
        list: A list of dictionaries, where each dictionary is one row from the
            input file.
    """
    final_list = []
    with open(input_filepath, "r") as csv_f:
        # read the file in csv format
        reader = csv.reader(csv_f)

        # extract headers
        headers = next(reader)

        for row in reader:
            # create new dictionary 
            d = {}
            # add key-value pairs into the dictionary
            # key,value have the same index in a row
            for i, value in enumerate(row):
                d[headers[i]] = value 

        # append the dictionary into a list
            final_list.append(d)

    return final_list   

#print(read_csv_file(infile))  

    


def write_csv_file(output_filepath, dict_to_write, header):
    """
    Writes a .csv file using the "csv" module. The file will contain the information
    from <dict_to_write>, where each row of the new .csv file is one of the key/value
    pairs. In other words, the output file should have two columns. Don't forget to
    include the header to each column, which is given to this function in the parameter
    <header>. The resultant file should be structured in the following way:

        <header[0]>,<header[1]>
        key1,value1
        key2,value2
        key3,value3
        ...etc

    Parameters:
        output_filepath (str): The file path to the new file being created.
        dict_to_write (dict): The information to include in the file being created.
        header (list): A list of two elements that correspond to the headers of the
            two columns in the new file.

    Returns:
        None, but writes a file.
    """

    with open(output_filepath, "w") as f:
        # write the file in csv format
        f_csv = csv.writer(f)

        # write the header
        f_csv.writerow(header)

        #write each key-value pair
        for k, v in dict_to_write.items():
            tuple_to_write = (k, v)
            f_csv.writerow(tuple_to_write)
        print("file is written successfully")


def acres_to_km2(acres):
    """
    Converts a value in acres to a value in kilometers squared. The conversion
    is as follows:

        1 acre is approximately 0.004 km^2

    Parameters:
        acres (float): A number in acres

    Returns:
        float: A number in km^2
    """

    km2 = acres * 0.004
    return km2


def km2_by_state(list_of_park_dicts):
    """
    This function takes a list of national park data (e.g. the returned value from
    <read_csv_file>), and returns a new dictionary that contains the summed
    area (in kilometers squared) of national parks in each state. The output
    dictionary should have the format:

    {<state two-letter identifier>: <float of total area of parks in that state in km^2>}

    Parameters:
        list_of_park_dicts (list): A list of dictionaries, where each dictionary contains the
            information on a specific park.

    Returns:
        dict: A dictionary where the keys are the two-letter state identifiers and the values
            are the sum total area of national parks in that state (in km^2).

    NOTE: Don't worry about states that don't have any national parks in the dataset we
    have provided. Your returned dictionary should only include the states that are present
    in the data.

    HINT: You'll need to use an accumulator pattern here to build a new dictionary. You
    will also need to call <acres_to_km2> to convert the park areas into km^2.
    """


#-----
    final_dict = {}

    for d in list_of_park_dicts:
        state = d['State']
        area = float(d['Acres'])
        km_area = acres_to_km2(area)

        if state not in final_dict.keys():
            final_dict[state] = 0
        final_dict[state] = final_dict[state] + km_area
    
    

    return  final_dict






def main():
    """
    Read in the data from "parks.csv". Then, parse that data and determine
    how much national park area is in each state using your <km2_by_state> function.
    Then, sort the resultant dictionary. Finally, write the sorted dictionary to a
    new file "parkarea.csv". Don't forget to include headers into the "parkarea.csv"
    file!

    Parameters:
        None

    Returns:
        None

    HINT: You will need to call each of the functions in this script to complete this
    task.
    """

    # read in the data
    park_list = read_csv_file(infile)
    # determine the area
    part_dict = km2_by_state(park_list)
    # sort the parks
    new_dict = sort_dictionary_by_value(part_dict)
    # write the file
    write_csv_file(outfile, new_dict, ("State", "Area"))




# END CODING HERE - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    main()
