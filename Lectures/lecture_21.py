import json
import requests

ENDPOINT = 'https://swapi.co/api'

class Entity:
    """Base representation of a resource. Instantiate with name
    and resource identifier.

        Attributes:
            name: resource name
            url: resource identifier

        Methods:
            assign_values: convenience method for loading in dict data
    """

    def __init__(self, name, url):
        self.name = name
        self.url = url # resource identifier


    def assign_values(self, data):
        """Bulk assign dictionary/map values. Iterate over object
        attributes (__dict__.keys()) and assign data values on matching
        keys using built-in setattr() function.

            Parameters:
                data (dict): key/value pairs to assign

            Returns:
                None
        """

        for key in self.__dict__.keys():
            if key in data.keys():
                setattr(self, key, data[key]) # handy built-in function


    def __str__(self):
        return self.name


class Person(Entity):
    """Representation of a person.

    Attributes:
        name: person name
        url: person's resource identifier
        gender: person's gender
        birth_year: person's birth_year
        homeworld: person's home planet

    Methods:
        get_homeworld: retrieve home planet
    """

    def __init__(self, name, url):
        super().__init__(name, url)
        self.gender = None
        self.birth_year = None
        self.homeworld = None


    def get_homeworld(self, url):
        """Retrieve SWAPI representation of home planet.
        Convert to Planet instance and assign to person.

        Parameters:
            url (str): resource identifier

        Returns:
            None
        """

        if not isinstance(self.homeworld, Planet):
            data = get_swapi_resource(url)
            homeworld = Planet(data['name'], data['url'])
            homeworld.assign_values(data)
            self.homeworld = homeworld


    def __str__(self):
        return self.name


class Planet(Entity):
    """Representation of a planet.

    Attributes:
        gravity: gravity level
        climate: climate description
        terrain: terrain description
        population: population size
    """

    def __init__(self, name, url):
        super().__init__(name, url)
        self.gravity = None
        self.climate = None
        self.terrain = None
        self.population = None


    def __str__(self):
        return self.name


class Starship(Entity):
    """A crewed vehicle used for traveling in realspace or hyperspace.

        Attributes:
            name: starship name or nickname
            url: resource identifier
            model: manufacturer's model name
            manufacturer: starship builder
            dimensions: starship length, width, height
            max_atmosphering_speed: TODO
            hyperdrive_rating: TODO
            MGLT: megalight per hour traveled
            crew: crew size
            crew_members: crew (role, name) assigned to starship
            passengers: number of passengers starship rated to carry
            cargo_capacity: cargo metric tonnage starship rated to carry
            consumables: max period in months before on-board provisions
                         must be replenished
            armament: offensive and defensive weaponry

    """

    def __init__(self, name, url):
        super().__init__(name, url)
        self.starship_class = None
        self.model = None
        self.manufacturer = None
        self.dimensions = None
        self.max_atmosphering_speed = None
        self.hyperdrive_rating = None
        self.MGLT = None # megalight per hour
        self.crew = None
        self.crew_members = {}
        self.passengers = None
        self.cargo_capacity = None
        self.consumables = None
        self.armament = []


    def assign_crew(self, crew):
        """Assign crew to crew_member dictionary.

        Parameters:
            crew (dict): key maps to role (e.g., pilot), value maps to
                         crew member name.

        Returns:
            None
        """

        for key, val in crew.items():
            self.crew_members[key] = val


    def __str__(self):
        return f"{self.starship_class} {self.model} {self.name}"


class ExtendedEncoder(json.JSONEncoder):
    """Extends json module's JSONEncoder class in order to serialize
     composite class instances.

     Methods:
        default: overrides default method
     """

    def default(self, obj):
        if isinstance(obj, Person):
            return {
                'url': obj.url,
                'name': obj.name,
                'gender': obj.gender,
                'birth_year': obj.birth_year,
                'homeworld': obj.homeworld
            }
        if isinstance(obj, Planet):
            return {
                'url': obj.url,
                'name': obj.name,
                'gravity': obj.gravity,
                'climate': obj.climate,
                'terrain': obj.terrain,
                'population': obj.population
            }
        if isinstance(obj, Starship):
            return {
                'url': obj.url,
                'name': obj.name,
                'starship_class': obj.starship_class,
                'model': obj.model,
                'manufacturer': obj.manufacturer,
                'dimensions': obj.dimensions,
                'max_atmosphering_speed': obj.max_atmosphering_speed,
                'hyperdrive_rating': obj.hyperdrive_rating,
                'MGLT': obj.MGLT,
                'crew': obj.crew,
                'crew_members': obj.crew_members,
                'passengers': obj.passengers,
                'cargo_capacity': obj.cargo_capacity,
                'consumables': obj.consumables,
                'armament': obj.armament
            }

        return json.JSONEncoder.default(self, obj)


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
        response = requests.get(url, params = params, timeout = timeout).json()
    else:
        response = requests.get(url, timeout = timeout).json()
    return response


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


def write_json(filepath, data):
    """Description removed. For you to write.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def write_complex_json(filepath, obj):
    """Serializes complex object structures (e.g., composite class
    instances). Adds an ExtendedEncoder to the json.dump() call.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(obj, file_obj, cls=ExtendedEncoder, ensure_ascii=False, indent=2)


def main():
    """Entry point for program. Orchestrates workflow involving
    reading in local data, issuing GET requests to retrieve remote data,
    instantiating class instances, and writing out data as JSON to a file.
    """

    # 1.0 DATA PREP

    # 1.1 Retrieve SWAPI representation of the Millenium Falcon (base)
    url = f"{ENDPOINT}/starships"
    params = {'search': 'falcon'}
    swapi_m_falcon = get_swapi_resource(url, params)["results"][0]

    print(f"\nSWAPI = {swapi_m_falcon}\n")

    # 1.2 Read in additional Millenium Falcon data
    filepath = 'wookiee_m_falcon.json'
    wookiee_m_falcon = read_json(filepath)

    print(f"\nLocal = {wookiee_m_falcon}\n")

    # 1.3 Combine starship data dicts
    # Note: local vals replace swapi vals on matching keys

    # UNCOMMENT
    swapi_m_falcon.update(wookiee_m_falcon) # in-place (no assignment)

    print(f"\nCombined = {swapi_m_falcon}\n")


    # 2.0 WORK WITH CLASS INSTANCES

    # 2.1 Create Starship instance
    m_falcon = Starship(swapi_m_falcon['name'], swapi_m_falcon['url'])

    # 2.2 Bulk assign dictionary values to instance variables
    # assign_values() acts as a filter
    # Downside: overwrites init values

    #UNCOMMENT
    m_falcon.assign_values(swapi_m_falcon)

    print(f"\nm_falcon.armament = {m_falcon.armament}\n")

    # 3.0 ASSIGN CREW TO STARSHIP
    url = f"{ENDPOINT}/people"

    # 3.1 Get SWAPI Han Solo (Corellian smuggler, pilot)
    params = {'search': 'solo'}
    swapi_solo = get_swapi_resource(url, params)['results'][0]

    print(f"\nswapi_solo = {swapi_solo}\n")

    # Add instance variable values the conventional way)
    solo = Person(swapi_solo["name"], swapi_solo['url']) # instantiate Person

    # UNCOMMENT
    solo.gender = swapi_solo['gender']
    solo.birth_year = swapi_solo["birth_year"]
    solo.get_homeworld(swapi_solo["homeworld"]) # fetch homeworld dict


    # 3.2 Get SWAPI Chewbacca (Wookiee, co-pilot)
    params = {'search': 'chewbacca'}
    swapi_chewie = get_swapi_resource(url, params)["results"][0]

    print(f"\nswapi_chewie = {swapi_chewie}\n")

    chewie = Person(swapi_chewie["name"], swapi_solo["url"]) # instantiate Person

    # UNCOMMENT
    chewie.assign_values(swapi_chewie) # bulk assign
    chewie.get_homeworld(swapi_chewie['homeworld']) # fetch homeworld dicts

    # 3.3 Assign crew
    crew = {"pilot": solo, "co-pilot": chewie} # key = role (pilot), value = name

    # UNCOMMENT
    m_falcon.assign_crew(crew)


    # 4.0 WRITE TO FILE
    filepath = 'si506_m_falcon.json'

    # UNCOMMENT (fail)
    write_json(filepath, m_falcon) # raises TypeError exception

    # Serialize composite class instances (a complex object)
    # Implement ExtendEncoder(); reference in json.dump()

    # UNCOMMENT (success)
    write_complex_json(filepath, m_falcon)


if __name__ == '__main__':
    main()
