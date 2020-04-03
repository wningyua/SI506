import requests, json

# # lab notes
# output = requests.get("https://swapi.co/api/people", params={"search": "Skywalker"}).json()
# print(output)

# LAB EXERCISE 10
# The following problems will introduce you to the requests module and
# to SWAPI API.  If a problem has a set-up, do NOT modify, delete, or ignore
# the set-up code.

ENDPOINT = "https://swapi.co/api"
PERSON_PROPERTIES = ('''
"name", "height", "mass", "hair_color", "skin_color",
 "eye_color", "birth_year", "gender", "homeworld", "films", "species", "starships", "url"
 ''')

# PROBLEM 1 (5 POINTS)
# In this problem you will demonstrate your understanding of the requests module by
# 1. Making a request
# 2. Encoding the response as a JSON object

def get_people(url, params=None):
    """This function initiates an HTTP GET request to a url to return a
    list of dictionaries. The function defines two parameters,
    the resource url (str) and an optional params (dict) query string of
    key:value pairs that may be provided as search terms (e.g., {'search': 'yoda'}).

    Parameters:
        url (str): the base url to look for response + resource
        params (dict): the parameters to specify the query.

    Returns:
        people (list): a list of dictionaries, each of which describes a person

    HINT: requests.get(url, params).json() returns a JSON Object that contains
    a "results" list properyty that contains a maximum of 10 records per request.
    Use the "results"key to index the dictionary representation of the
    decoded JSON to access the resource(s) matched by the search query return.

    """
    output = requests.get(url, params).json()
    output = output["results"]
    return output

# PROBLEM 2 (5 points)
# In this problem, you will demonstrate your understanding of
# 1) working with conditional statements
# 2) working with dictionaries
# 3) working with for loops

def filter_properties(person, PERSON_PROPERTIES):
    """
    Extract specific properties of the given person into a new dictionary.

    Parameters:
        person (dict): the dictionary containing properties of a person.
        PERSON_PROPERTIES (tupl): a tuple containing the charachteristics of a person

    Returns:
        record (dict): a dictionary containing filtered key-value pairs
        of characteristics of the person.

    """
    record = {}
    for key, val in person.items(): 
        # loop through dictionary 
        if key in PERSON_PROPERTIES:
            record[key] = val
    return record


# PROBLEM 3 (5 points)
# In this problem, you will demonstrate your understanding of writing a JSON file.

def write_json(filepath, data):
    """Given a valid filepath writes data to a JSON file.
    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.
    Returns:
        None

    HINT: for the open parameters, use encoding= 'utf-8' and for the
    json.dump parameters, use ensure_ascii= False, indent=2.
    """
    with open(filepath, "w") as f:
        json.dump(data, f, ensure_ascii= False, indent=2)

# PROBLEM 4 (5 POINTS)

def main():
    '''
    This function executes the following code:
    1. Uiltizes <get_people> function to make request to URL to get list of dictionaries
     representing people called <people>. Use the search parameter to only return people
     that have "Skywalker" in their name.
    2. Loops through list of dictionaries called <people>
    3. Inside the loop, use function <filter_properties> for the items in <people>
    to get a new record of each person listed in <people>.
    4. Append the new record to an accumulator
    5. Write results to file called "swapi_people.json."

    Parameters: None

    Returns: None

    HINT: Review SWAPI documentation on how to make a call to people section.
    '''
    url = f"{ENDPOINT}/people/"
    people = get_people(url, params={"search": "Skywalker"})
    #print(people)

    new_people_records = []

    for person in people:
        new_person = filter_properties(person, PERSON_PROPERTIES)
        new_people_records.append(new_person)

    write_json("swapi_people.json", new_people_records)

if __name__ == '__main__':
    main()

# END LAB EXERCISE
