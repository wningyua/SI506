import json
import requests

# LECTURE 22 Objectives

# Objectives
# 1. Get to know list comprehensions
# 2. Get to know dictionary comprehensions
# 3. Work with SWAPI API

ENDPOINT = 'https://swapi.co/api'

def convert_string_to_int(val):
    """Attempts to convert a string to an int.  If unsuccessful returns
    the value unchanged. Note that this function will return True for
    boolean values, faux string boolean values (e.g., "true"), "NaN",
    exponential notation, etc.

    See https://stackoverflow.com/questions/379906/how-do-i-parse-a-string-to-a-float-or-int

    Parameters:
        value (str): string to be converted.

    Returns:
        int: if string successfully converted.
        str: if string could not be converted.

    """

    try:
        return int(val)
    except ValueError:
        return val


def era_year(date):
    """Separate the Galatic date into era (e.g., BBY, ABY) and year.

    Parameters:
        date (str): Galatic year and era (e.g., 19BBY)

    Returns:
        tuple: era, year

    """

    return date[-3:], float(date[:-3]) # pack; take the last three components


def get_swapi_resource(url, params=None, timeout=20):
    """Description removed. For you to write.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        response = requests.get(url, params=params, timeout=timeout).json()
    else:
        response = requests.get(url, timeout=timeout).json()

    return response


def is_unknown(val):
    """Check if value is in list of unknown values. If value
    is not a string catch the AttributeError raised by use of
    str.lower() and return False.
    """

    unknown_vals = ('unknown', 'n/a')

    try:
        return val.lower() in unknown_vals # truth value
    except AttributeError: # not a str
        return False


def read_json(filepath):
    """Description removed. For you to write.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict: dictionary representations of the decoded JSON document.
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)

    return data


def main():
    """Entry point for program. Orchestrates workflow."""

    # 1.0 DATA SET (JEDI)
    filepath = 'swapi_jedi.json'
    swapi_jedi = read_json(filepath)


    # 2.0 LIST COMPREHENSION EXAMPLES

    # 2.1 JEDI NAME LIST
    # Loop over swapi_jedi and append names to the name list.

    # 2.1.1 for loop (list of strings)

    jedi_names_01 = []
    for jedi in swapi_jedi:
        jedi_names_01.append(jedi['name']) # much slower

    print(f"\nJedi names for loop = {jedi_names_01}\n")

    # 2.1.2 list comprehension (list of strings)
    # format: [<expression> for <element> in <sequence>]

    jedi_names_02 = [jedi["name"] for jedi in swapi_jedi]

    print(f"\nJedi names list comp = {jedi_names_02}\n")


    # 2.2 JEDI NAME, BIRTH YEAR LIST
    # Loop over swapi_jedi and append to new list
    # {'name': <name>, 'birth_year': <birth_year>}.

    # 2.2.1 for loop

    jedi_birth_years_01 = []
    for jedi in swapi_jedi:
        record = {'name': jedi['name'], 'birth_year': jedi['birth_year']}
        jedi_birth_years_01.append(record)

    print(f"\nJedi birth year for loop = {jedi_birth_years_01}\n")

    # 2.2.1 list comprehension (list of dictionaries)
    # format: [<dict literal> for <element> in <sequence>]

    # Note: writing a comprehension is not limited to a single line.

    jedi_birth_years_02 = [{'name': jedi['name'], 'birth_year': jedi['birth_year']} for jedi in swapi_jedi]

    print(f"\nJedi birth year list comp = {jedi_birth_years_02}\n")


    # 2.3 CONDITIONAL STATEMENT
    # Filter: Jedi with surname 'Skywalker' (name only)

    # 2.3.1 for loop

    skywalkers_01 = []
    for jedi in swapi_jedi:
        if 'skywalker' in jedi['name'].lower():
            skywalkers_01.append(jedi['name'])

    print(f"\nSkywalkers for loop = {skywalkers_01}\n")

    # 2.3.2 list comprehension
    # format: [<expression> for <element> in <sequence> if <condition>]

    skywalkers_02 = [j['name'] for j in swapi_jedi if 'skywalker' in j['name'].lower()]
    print(f"\nSkywalkers list comp = {skywalkers_02}\n")


    # 2.4 CONDITIONAL STATEMENT
    # Filter: Human Jedi (name only)

    # SWAPI GET request (identify human species)

    # UNCOMMENT
    url = ENDPOINT + '/species'
    params = {'search': 'human'}
    response = get_swapi_resource(url, params)
    human = response['results'][0]

    # One line dictionary assignment
    # human = get_swapi_resource(url, params)['results'][0]

    # 2.4.1 for loop

    # UNCOMMENT
    jedi_humans_01 = []
    for jedi in swapi_jedi:
        if jedi['species'][0] == human['url']:
            jedi_humans_01.append(jedi['name'])

    print(f"\nJedi humans for loop = {jedi_humans_01}\n")

    # 2.4.2 list comprehension

    jedi_humans_02 = [j["name"] for j in swapi_jedi if j['species'][0] == human['url']]

    print(f"\nJedi humans list comp = {jedi_humans_02}\n")


    # 2.5 CALL FUNCTION
    # Call two functions: is_unknown(val) and era_year(date)

    # Filter: Jedi assassinated following activation of
    # the Infamous Clone Protocol 66 (Order 66) in 19 BBY.
    # See https://starwars.fandom.com/wiki/Order_66

    # 2.5.1 for loop

    order_66_01 = []
    for jedi in swapi_jedi:
        if not is_unknown(jedi['death_year']):
            era, year = era_year(jedi['death_year']) # unpack
            if era == 'BBY' and year == 19.0:
                order_66_01.append(jedi['name'])

    print(f"\nOrder 66 for loop = {order_66_01}\n")

    # 2.5.2 list comprehension

    order_66_02 = [
        j['name'] for j in swapi_jedi if
        not is_unknown(j['death_year']) and 
        era_year(jedi['death_year'])[0] == "BBY" and 
        era_year(jedi['death_year'])[1] == 19.0
    ]

    print(f"\nOrder 66 list comp = {order_66_02}\n")


    # 2.6 IF-ELSE STATEMENT
    # Filter: Identify Human vs non-Human Jedi and apply label

    # 2.6.1 for loop

    # UNCOMMENT
    jedi_species = []
    for jedi in swapi_jedi:
        if jedi['species'][0] == human['url']:
            person = (jedi['name'], 'Human') # tuple
        else:
            person = (jedi['name'], 'Non-human') # tuple

        jedi_species.append(person)

    print(f"\nJedi human/non-human for loop = {jedi_species}\n")

    # 2.6.2 list comprehension
    # Note: you may well conclude that the comprehension below
    # compromises readability

    jedi_species = [
        (jedi['name'], 'Human') 
        if jedi['species'][0] == human['url']
        else (jedi['name'], 'Non-human') 
        for jedi in swapi_jedi
    ]

    print(f"\nJedi human/non-human list comp = {jedi_species}\n")


    # 3.0 DICTIONARY COMPREHENSION

    # 3.1 CREATE A DICTIONARY FROM A LIST OF DICTIONARIES
    # format: {<key>: <value> for <element> in <sequence>}

    jedi_urls = {j["name"]: j["url"] for j in swapi_jedi}

    print(f"\nJedi URLs = {jedi_urls}\n")


    # 3.2 CONDITIONAL STATEMENT
    # Loop over list and extract female Jedi into new dictionary

    # 3.2.1 for loop

    female_jedi_01 = {}
    for jedi in swapi_jedi:
        if jedi['gender'].lower() == 'female':
            female_jedi_01[jedi['name']] = {
                'gender': jedi['gender'],
                'url': jedi['url']
            }

    print(f"Female Jedi for loop = {female_jedi_01}\n")

    # 3.2.2 dictionary comprehension

    female_jedi_02 = {
        j["name"]: {'gender': j['gender'], 'url': j['url']}
        for j in swapi_jedi
        if j['gender'].lower() == 'female'
    }

    print(f"Female Jedi dict comp = {female_jedi_02}\n")

    # 3.3 CONDITIONAL STATEMENT
    # Loop over filter keys and extract matching key/value pairs
    # into new dictionary

    filter_keys = ('name', 'height', 'mass', 'url')
    swapi_yoda = swapi_jedi[3]

    # 3.3.1 for loop
    yoda_01 = {}
    for key in filter_keys:
        if key in swapi_yoda.keys():
            yoda_01[key] = swapi_yoda[key]

    print(f"\nYoda for loop = {yoda_01}\n")

    # 3.3.2 dictionary comprehension
    yoda_02 = {key: swapi_yoda[key] 
    for key in filter_keys 
    if key in swapi_yoda.keys()
    }
    print(f"\nYoda dict comp = {yoda_02}\n")


    # 3.4 IF-ELSE STATEMENT
    # call convert_string_to_int(val) if key in int_props

    int_props = ('height', 'mass')

    # 3.4.1 for loop
    yoda_03 = {}
    for key, val in yoda_01.items():
        if key in int_props:
            yoda_03[key] = convert_string_to_int(val)
        else:
            yoda_03[key] = val

    print(f"\nYoda for loop int vals  = {yoda_03}\n")

    # 3.4.2 dictionary comprehension
    # format: {
    # (<new key> if <condition> else <key>):
    # (<new val> if <condition> else else <val>)
    # for key, val in dict_.items()
    # }

    # Note: an if-else condition for both key and val is not required
    # if one or the other is not impacted by the condition.

    yoda_04 = {
        key: convert_string_to_int(val) if key in int_props else val
        for key, val in yoda_01.items()
    }

    print(f"\nYoda dict comp int vals = {yoda_04}\n")

if __name__ == '__main__':
    main()