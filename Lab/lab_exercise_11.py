import requests, json

# lab notes
# cat_names = ["Ginger", "Crookshanks", "Shadow", "Whiskers"]
# print(cat_names)

# # list comprehension
# cat_introductions = [f"{cn} is my cat!" for cn in cat_names]
# print(cat_introductions)

# # dictionary comprehension
# length_of_name = {cn: len(cn) for cn in cat_names}
# print(length_of_name)

# # conditional comprehension
# length_of_name = {cn: (len(cn) if len(cn) < 8 else "Too Long") 
# for cn in cat_names}
# print(length_of_name)


# LAB EXERCISE 11

# The following lab exercise will allow you to work more with SWAPI to get you
# comfortable with using requests module as you work on your final assignement.
# This week, we are looking at the planets in the SWAPI. We will   
# be learning about classes, dictionary and list comprehensions.

# If a problem has a set-up, do NOT modify, delete, or ignore
# the set-up code.

# SETUP CODE
ENDPOINT = 'https://swapi.py4e.com/api/planets'
PLANETS = ["Tatooine", "Yavin", "Coruscant", "Hoth"]

class JsonSerializable(object):
    '''
    This class helps make the <Planet> class serializable
    so that we can store its instances into a json file
    '''
    def to_dict(self):
        '''
        This function writes the instance variables of
        teh object to a dictionary

        Returns:
            dictionary of current instance
        '''
        return self.__dict__

    def __repr__(self):
        '''
        This function holds the printable representation of
        the object which in this case is the dictionary object
        which is obtained by calling toJson

        Returns:
            printable representation of the object
        '''
        return self.to_dict()
# END SETUP

# PROBLEM 1 (2.5 points)

# In this problem you will:
# 1) Create a class
# 2) Initialize it

# Create a class named <Planet> and initialize it.
    
class Planet(JsonSerializable):
    '''
    This is a class that stores information about Planets in the Star Wars universe

    Attributes:
        name(str) -- The name of this planet.
        diameter(str) -- The diameter of this planet in kilometers.
        rotation_period(str) -- The number of standard hours it takes for this planet to complete a single rotation on its axis.
        orbital_period(str) -- The number of standard days it takes for this planet to complete a single orbit of its local star.
        gravity(str) -- A number denoting the gravity of this planet, where "1" is normal or 1 standard G. "2" is twice or 2 standard Gs. "0.5" is half or 0.5 standard Gs.
        population(str) -- The average population of sentient beings inhabiting this planet.
        climate(str) -- The climate of this planet. Comma separated if diverse.
        terrain(str) -- The terrain of this planet. Comma separated if diverse.
        surface_water(str) -- The percentage of the planet surface that is naturally occurring water or bodies of water.
        residents(list) -- An array of People URL Resources that live on this planet.
        films(list) -- An array of Film URL Resources that this planet has appeared in.
        created(str) -- the ISO 8601 date format of the time that this resource was created.
        edited(str) -- the ISO 8601 date format of the time that this resource was edited.
        url(str) -- the hypermedia URL of this resource.
    '''

    def __init__(self,name, diameter, rotation_period, orbital_period, gravity, population, climate, 
    terrain, surface_water, residents, films, created, edited, url):
        '''
        This is the initialization function of the <Planet> class. Here you will 
        need to create the instance variables for the parameters described in this docstring. 
        Note that the attributes mentioned in the class definition are defined by parameters 
        passed to this constructor method.

        Parameters:
            name(str) -- The name of this planet.
            diameter(str) -- The diameter of this planet in kilometers.
            rotation_period(str) -- The number of standard hours it takes for this planet to complete a single rotation on its axis.
            orbital_period(str) -- The number of standard days it takes for this planet to complete a single orbit of its local star.
            gravity(str) -- A number denoting the gravity of this planet, where "1" is normal or 1 standard G. "2" is twice or 2 standard Gs. "0.5" is half or 0.5 standard Gs.
            population(str) -- The average population of sentient beings inhabiting this planet.
            climate(str) -- The climate of this planet. Comma separated if diverse.
            terrain(str) -- The terrain of this planet. Comma separated if diverse.
            surface_water(str) -- The percentage of the planet surface that is naturally occurring water or bodies of water.
            residents(list) -- An array of People URL Resources that live on this planet.
            films(list) -- An array of Film URL Resources that this planet has appeared in.
            created(str) -- the ISO 8601 date format of the time that this resource was created.
            edited(str) -- the ISO 8601 date format of the time that this resource was edited.
            url(str) -- the hypermedia URL of this resource.
            
        Returns:
            None

        '''
        self.name = name
        self.diameter = diameter
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.gravity = gravity
        self.population = population
        self.climate = climate
        self.terrain = terrain
        self.surface_water = surface_water
        self.residents = residents
        self.films = films
        self.created = created
        self.edited = edited
        self.url = url

# END PROBLEM 1

# PROBLEM 2 (10 points)

# In this problem you will:
# 1) Create a GET request
# 2) Parse JSON and work with keys and values
# 3) Use list comprehension

def get_planets(name):
    '''
    This method send a GET reuest to the SWAPI and creates an instance
    of <Planet> class and returns the instance.

    Parameters:
        name(str): Name of the planet
    
    Returns:
        returns a <Planet> object instance
    '''
    # Send a GET request to SWAPI using '{'search': name}' as params
    # and store it as dictionary.  
    response = requests.get(ENDPOINT, params = {'search': name}).json()
    print(response)
    # Use the "results" key and index the dictionary representation of the
    # decoded JSON to access the resource(s) matched by the search query return.
    # Store this as <result>
    # HINT: response['results'][0]
    # HINT: convert your <response> to JSON object using response.json()
    result = response["results"][0]

    # Using list comprehension, find the values from <result> and store them
    # in a list named <planet_props>
    planet_props = [value for key, value in result.items()]


    # Create an instance of <Planet> object and pass <planet_prop> list's elements
    #  as arguments using the '*' operator as a variable args call and return the instance.
    # Hint: Planet(*planet_props)
    planet = Planet(*planet_props) # passing all elements from the list
    # print(planet.to_dict())
    return planet

# print("\n\nHERE: ")
# get_planets("Tatooine")   

# END PROBLEM 2 

# PROBLEM 3 (2.5 points)
# In this problem you will
# 1) Write into a JSON file

def write_json(filepath, data):
    '''
    Given a valid filepath writes data to a JSON file.
    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.
    Returns:
        None

    HINT: for the open parameters, use encoding= 'utf-8' and for the
    json.dump parameters, use ensure_ascii= False, indent=2.
    '''
    with open(filepath, "w", encoding= 'utf-8' ) as f:
        json.dump(data, f, indent=2)


# END PROBLEM 3

# PROBLEM 4 (5 points)

# In this problem you will:
# 1) Use Dictionary comprehension
# 2) Call other functions   

def main():
    '''
    This function calls <get_planet> function to retrieve SWAPI planer data. Then it 
    calls <write_json> function to store the data to a json file.

    parameters:
        None
    Return:
        None
    '''
    # Using dictionary comprehension, store the name of planets from <PLANETS> as Keys
    # and call the <get_planets> function to get instances for each planet and
    # store it as values. Store the dictionary as <planets_data>. Call <to_dict>
    # on your planet instance to make it serializable (Example: get_planet<'name'>.to_dict())
    planets_data = {p: get_planets(p).to_dict()  for p in PLANETS}
    # print(planets_data.keys())


    # Write the planets_data as "swapi_planets.json" by calling
    # the <write_json> function.
    write_json("swapi_planets.json", planets_data)
    

 # END PROBLEM 4   
    
    
    print('Write completed')
if __name__ == '__main__':
    main()

# END OF LAB EXEFRCISE