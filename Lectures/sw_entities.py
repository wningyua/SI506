from sw_utilities import get_swapi_resource

INT_PROPS = (
    'rotation_period',
    'orbital_period',
    'diameter',
    'surface_water',
    'population'
)

LIST_PROPS = (
    'climate',
    'terrain'
)


class Entity:
    """Base representation of a resource. Instantiate with name
    and resource identifier.

    Attributes:
        name: resource name
        url: resource identifier

    Methods:
        assign_values: convenience method for loading in dict data
        jsonable: return JSON-friendly dict representation of the object
    """

    KEYS = (
        'url',
        'name'
    )

    def __init__(self, name, url):
        self.name = name
        self.url = url


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
                setattr(self, key, data[key])


    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and
        mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {'name': self.name, 'url': self.url}


    def __str__(self):
        return self.name


class Planet(Entity):
    """Representation of a planet.

    Attributes:
        gravity: gravity level
        climate: climate description
        terrain: terrain description
        population: population size

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    KEYS = (
        'url',
        'name',
        'rotation_period',
        'orbital_period',
        'diameter',
        'climate',
        'gravity',
        'terrain',
        'surface_water',
        'population'
    )

    def __init__(self,
        name,
        url,
        rotation_period,
        orbital_period,
        diameter,
        climate,
        gravity,
        terrain,
        surface_water,
        population
        ):

        super().__init__(name, url)
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.surface_water = surface_water
        self.population = population


    def jsonable(self):
        """Return a JSON-friendly representation of the object.
        Use a dictionary literal rather than built-in dict() to avoid
        built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and
        mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        # return self.__dict__ # DANGEROUS
        # return copy.deepcopy(self.__dict__) # safe but slow

        return {
                'url': self.url,
                'name': self.name,
                'rotation_period': self.rotation_period,
                'orbital_period': self.orbital_period,
                'diameter': self.diameter,
                'climate': self.climate,
                'gravity': self.gravity,
                'terrain': self.terrain,
                'surface_water': self.surface_water,
                'population': self.population
            }


    def __str__(self):
        return self.name
