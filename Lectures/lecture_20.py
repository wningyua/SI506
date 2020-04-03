import requests

# LECTURE 20 Objectives

# Objectives
# 1. Install the requests module using pip (pre-req).
# 2. Learn how to use the requests package to sent
#    GET requests to an endpoint.
# 3. Understands the basics of HTTP request/response messages.
# 4. Learn how to retrieve data from the Star Wars API.
# 5. Write a function to retrieve SWAPI resources.


# 1.0 REQUEST MESSAGE ANATOMY
# Request line
#   method token, e.g. GET
#   request URI, e.g. https://swapi.co/api/people/4/
#   HTTP protocol version, e.g. HTTP/1.1
# 0 or more Request headers (message metadata)
# Optional body (PUT/POST methods transmit content)


# 1.1 SWAPI ENDPOINT (REMOTE SERVICE)
# Only accepts GET requests (no PUT, POST, DELETE requests accepted)
ENDPOINT = 'https://swapi.co/api'

# print(f"\nEndpoint = {ENDPOINT}\n")


# 1.2 SWAPI: REQUEST LIST OF AVAILABLE RESOURCES
# /api/

response = requests.get('https://swapi.co/api/') # note trailing slash

# print(f"\nRoot response = {response.json()}\n") # .json() convert to dict


# 1.3 SWAPI: REQUEST RESOURCES BY CATEGORY (PAGED RESPONSE n=10 records)
# /api/:category/
# See swapi_people_page_01.json

response = requests.get('https://swapi.co/api/people/').json()
total_count = response['count']
people_returned = len(response['results']) # paged results (discussed below)

# print(f"People count = {total_count}; records returned = {people_returned}\n")


# 1.4 SWAPI: REQUEST SINGLE RESOURCE
# /api/people/:id/

response = requests.get('https://swapi.co/api/people/4/')

# Example: request headers specified
# response = requests.get(
#     'https://swapi.co/api/people/4/',
#     headers={"Accept": "application/json"}
#     )


# 2.0 RESPONSE MESSAGE ANATOMY
# Status line
#   HTTP version, e.g. HTTP/1.1
#   Status code and reason, e.g. 200 OK
# 0 or more request headers (message metadata)
# Optional body


# 2.1 STATUS CODE / REASON
# See https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

status_code = response.status_code
reason = response.reason

# print(f"\nstatus code & reason = {status_code} {reason}\n")

# Also a code lookup is available.
if response.status_code == requests.codes.ok:
    print(f"OK: standard SWAPI response received for successful HTTP request.\n")
else:
    print(f"Not OK: Non-standard or bad SWAPI response received.\n")


# 2.2 RESPONSE HEADERS
# Response metadata

headers = response.headers # a dictionary
if headers:
    string = ''
    for key, val in headers.items():
        string += f"{key} = {val}\n"

# print(f"\n HEADERS\n {string}")


# 2.3 RESPONSE HEADERS: CONTENT-TYPE
# i.e., media type, formerly mime type

content_type = response.headers['Content-Type']

# print(f"\nSWAPI Response Content-Type = {content_type}\n")


# 2.4 RESPONSE CONTENT/BODY

body = response.text # returns string (not useful for SWAPI payloads)
encoding = response.encoding

# print(f"\nResponse text type = {type(body)}\n")
# print(f"\nResponse text = {body}\n")
# print(f"\nResponse encoding = {encoding}\n") # doesn't return value


# 2.5 CONVERT JSON TO LISTS AND DICTIONARIES
# Recall SWAPI Content-Type = application/json

# You can convert JSON to a dictionary by calling the .json() method
# See darth_vader.json for pre-conversion view

body = response.json() # returns dictionary

print(f"\nSWAPI representation of Darth Vader\n")
for key, val in body.items():
    print(f"{key} = {val}")


# 2.6 YOU CAN ALSO DO THIS (method chaining)

vader = requests.get('https://swapi.co/api/people/4/').json()

# print(f"\nrequests.get(</api/people/4/>).json() = {vader['name']}\n")


# 3.0 EXCEPTIONS (CODE DEFENSIVELY)
# Information retrieval sometimes fails

# 3.1 HTTP Errors
# Response received but not expected response.

try:
    # Bad id
    response = requests.get('https://swapi.co/api/people/0/')
    response.raise_for_status() # raise HTTPError for 4xx or 5xx status codes

    # Bad endpoint
    # response = requests.get('https://swapi.co/api/person/4/')
    # response.raise_for_status() # raise HTTPError for 4xx or 5xx status codes
except requests.exceptions.HTTPError as err:
    # raise SystemExit(e) # exit program and print error
    print(f"{err}\n")


# 3.2 TIMEOUTS
# Good practice: set a local timeout (seconds)

try:
    # Generate a timeout deliberately
    response = requests.get('https://swapi.co/api/people/4/', timeout = 0.001)

except requests.exceptions.RequestException as err:
    # raise SystemExit(e) # exit program and print error
    print(f"{err}\n")


# 3.3 CONNECTION ERRORS
# Server down, mangled URL, etc.

try:
    # Generate ConnectionError but set timeout to limit wait time
    response = requests.get('https://efgjdldlgdsdgsdfgsdg', timeout=15)
except requests.exceptions.RequestException as err:
    # raise SystemExit(e) # exit program and print error
    print(f"{err}\n")

# Note: you can also implement a try block with multiple except blocks in
# order to handle each request exception (ConnectionError, HTTPError, Timeout,
# and TooManyRedirects) individually.


# 4.0 PASSING PARAMETERS
# Request URI with query string
# https://swapi.co/api/people/?search=yoda

# The requests module accepts query string values as key/value pairs
# params = {'key1': 'val1', 'key2': 'val2', . . .}

# 4.1 SWAPI search limitations
# See https://swapi.co/documentation
# 1. only accepts two query string types
#    a. search=<string> (name, title, or model depending on entity)
#    b. page=<num>
# 2. Searches employ case-insensitive partial matches on search fields.

response = requests.get(
    'https://swapi.co/api/people/',
    {'search': 'darth'},
    timeout=10
    ).json()

# 4.1.1 TAKE HEED: SWAPI SEARCH RESULTS RETURNED IN A JSON "ENVELOPE".
# See sith_lords.json

print(f"\nDarth Search = {response}\n")

# Get Search results (e.g., Darth Maul and Darth Vader)

sith_lords = response['results'] # a list of dictionaries

print(f"Sith Lords (bad guys)")
for sith in sith_lords:
    print(f"{sith['name']}")

# 4.1.2: TAKE HEED: SWAPI RESPONSES ARE "PAGED"
# SWAPI returns 10 records max

# GET PLANETS

response = requests.get(
    'https://swapi.co/api/planets/',
    timeout=10
    ).json()

# 61 planets but only 10 returned at a time
# See swapi_planets_page_01.json

print(f"\nPlanets total = {response['count']}\n")
print(f"Planets results count = {len(response['results'])}\n")

# GET People with letter 'r' in name

response = requests.get(
    'https://swapi.co/api/people/',
    {'search': 'r'},
    timeout=10
    ).json()

print(f"letter 'r' in name count = {response['count']}\n")

# Rey missing (only first 10 records returned)

people = response['results']
for person in people:
    print(person['name'])

print('\n') # padding

# Rey found

people = requests.get(
    'https://swapi.co/api/people/',
    {'search': 'r', 'page': 5}, # add page (hack)
    # {'search': 'r', 'ordering': '-name'}, # ordering ignored
    timeout=10
    ).json()['results'] # return list

for person in people:
    print(person['name'])

# print('\n') # padding

# Note: one can solve the paging challenge by writing a recursive function
# that calls itself repeatedly in order to return every paged set of records.
# But such a function is out of scope for SI 506.


# 5.0 A FUNCTION

def get_swapi_resource(url, params=None, timeout=10):
    """Description removed. You will soon write it.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        response = requests.get(url, params = params, timeout = timeout).json()
    else:
        response = requests.get(url, timeout = timeout).json()

    return response

# 5.1 CALL FUNCTION

# Search and retrieve the astromech droid R2-D2
url = f"{ENDPOINT}/people/"
parameter = {"search": "r2"}

# Call function, pass args
response = get_swapi_resource(url, parameter)
r2_d2 = response["results"][0]

print(f"R2-D2 = {r2_d2}\n")
