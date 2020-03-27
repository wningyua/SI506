import uuid

# Class definitions based on the following draft W3C specification:
# Building Topology Ontology
# https://w3c-lbd-cg.github.io/bot/
# The Building Topology Ontology (BOT) is described as "a minimal ontology
# for describing the core topological concepts of a building.""

class Zone:
    """A spatial 3D division that groups space. Sub-classes of Zone
    include Site, Building, Story, and Space.

    This class could be marked as an abstract class (out of scope for SI 506).

    Attributes:
        type_iri: type identifier
        id_: zone identifier
        name: name of zone
    """

    type_iri = 'https://w3c-lbd-cg.github.io/bot/#Zone' # class variable

    def __init__(self, name):
        """Initialize instance.

        Parameters:
            id_ (UUID): zone identifier
            name (str): name of zone

        Returns:
            None
        """

        self.id_ = uuid.uuid4() # auto generate (add _ avoids clash with id())
        self.name = name

    def __str__(self):
        """Informal string representation of object.

        Parameters:
            None

        Returns:
            str: name of object
        """

        return f"{self.name}"


class Site(Zone):
    """An area containing one or more buildings.

    Attributes:
        type_iri: type identifier
        id_: site identifier
        name: name of site
        latitude: latitudinal coordinate of site
        longitude: longitudinal coordinate of site
        TODO: add area
    """

    type_iri = 'https://w3c-lbd-cg.github.io/bot/#Site'

    def __init__(self, name, latitude, longitude):
        """Initialize instance.

        Parameters:
            id_ (UUID): site identifier
            name (str): name of site
            latitude (float): latitudinal coordinate of site
            longitude (float): longitudinal coordinate of site
            buildings (list): buildings comprising site
            TODO: add area

        Returns:
            None
        """

        super().__init__(name)
        self.id_ = uuid.uuid4() # auto generate (add _ avoids clash with id())
        self.latitude = latitude
        self.longitude = longitude
        self.buildings = []


    def __str__(self):
        """Informal string representation of object.

        Parameters:
            None

        Returns:
            str: name of object and geo coordinates
        """

        return f"{self.name}: {self.latitude} (lat.) {self.longitude} (long.)"


class Building(Zone):
    """An independent unit of the built environment with a characteristic
    spatial structure, intended to serve at least one function or user
    activity [ISO 12006-2:2013]. Example of a composite class.

    Attributes:
        type_iri: type identifier
        id_: building identifier
        name: name of building
        latitude: latitudinal coordinate of site
        longitude: longitudinal coordinate of site
        stories: list of stories associated with building
        TODO: add postal address

    Methods:
        add_story: adds a story to building
        add_stories: adds a sequence of stories to building
        num_stories: counts number of stories possessed by building
    """

    type_iri = 'https://w3c-lbd-cg.github.io/bot/#Building'

    def __init__(self, name, latitude, longitude):
        """Initialize instance.

        Parameters:
            id_ (UUID): building identifier
            name (str): name of building
            latitude (float): latitudinal coordinate of building
            longitude (float): longitudinal coordinate of building
            stories (list): stories comprising building
            TODO: add postal address

        Returns:
            None
        """

        super().__init__(name)
        self.id_ = uuid.uuid4() # auto generate (add _ avoids clash with id())
        self.latitude = latitude
        self.longitude = longitude
        self.stories = [] # component (has_a relationship)


    def add_story(self, story):
        """Appends a story to the building object's sequence of stories.

        Parameters:
            story (Story): a story to be added to the building

        Returns:
            None
        """

        self.stories.append(story)


    def add_stories(self, stories):
        """Extends the building's list of stories with another list of
        stories.

        Parameters:
            stories (list): sequence of story objects to be added to building

        Returns:
            None
        """

        self.stories.extend(stories)


    def num_stories(self):
        """Counts the number of stories possessed by building.
        Note: a basement is considered a below-grade story.

        Parameters:
            None

        Returns:
            int: number of stories in a given building
        """

        return len(self.stories)


    def __str__(self):
        """Informal string representation of object.

        Parameters:
            None

        Returns:
            str: name of object, geo coordinates, stories and rooms
        """

        string = f"{self.name} ({self.longitude}, {self.latitude})\n"
        if self.stories:
            for story in self.stories:
                string += f"  {story.name}\n"
                if story.spaces:
                    for space in story.spaces:
                        string +=f"    {space.name}"
                        if space.format_dimensions():
                            string += f" {space.format_dimensions()}"
                        string += '\n'

        return string


class Story(Zone):
    """A level part of a building. Example of a composite class.

    Attributes:
        type_iri: type identifier (not the same as an instance id)
        id_: story identifier
        name: name of story
        number: number of story
        spaces: list of spaces associated with story
        building: parent building

    """

    type_iri = 'https://w3c-lbd-cg.github.io/bot/#Storey'

    def __init__(self, name, building):
        """Initialize instance.

        Parameters:
            id_ (UUID): story identifier
            name (str): name of story
            number (int): number of story
            spaces (list): spaces comprising story
            building (Buidling): parent building

        Returns:
            None
        """

        self.id_ = uuid.uuid4() # auto generate (add _ avoids clash with id())
        self.name = name
        self.number = None
        self.spaces = [] # component (has_a relationship)
        self.building = building # component (is_part_of relationship)


    def add_space(self, space):
        """Appends a space to the story object's sequence of spaces.

        Parameters:
            space (space): a space to be added to the story

        Returns:
            None
        """

        self.spaces.append(space)


    def add_spaces(self, spaces):
        """Extends the story's list of spaces with another list of
        spaces.

        Parameters:
            spaces (list): sequence of space object to be added to story

        Returns:
            None
        """

        self.spaces.extend(spaces)


    def num_spaces(self):
        """Counts the number of spaces possessed by story.

        Parameters:
            None

        Returns:
            int: number of spaces in a given story
        """

        return len(self.spaces)


    def __str__(self):
        """Informal string representation of object.

        Parameters:
            None

        Returns:
            str: name of object and associated building name
        """

        return f"{self.building.name}, {self.name}"


class Space(Zone):
    """A limited three-dimensional extent defined physically or
    notionally [ISO 12006-2 (DIS 2013), 3.4.3]

    Attributes:
        type_iri: type identifier (not the same as an instance id)
        id_: space identifier
        format_dimensions: human readable space dimensions

    """

    type_iri = 'https://w3id.org/bot#Space'

    def __init__(self, name, dimensions, story):
        """Initialize instance.

        Parameters:
            id_ (UUID): space identifier
            name (str): name of building
            dimensions (dict): length and width of space
            story (Story): parent story

            TODO: add height to dimensions dict

        Returns:
            None
        """

        super().__init__(name)
        self.id_ = uuid.uuid4() # auto generate (add _ avoids clash with id())
        self.number = None
        self.dimensions = dimensions
        self.story = story # component (is part of relationship)


    def format_dimensions(self):
        """Returns human readable space dimensions.

        TODO: Add height

        Parameters:
            None

        Returns:
            str: formatted dimensions of space
        """

        # Note use of escape characters \' and \"
        if self.dimensions['length_ft'] and self.dimensions['width_ft']:
            length = f"{self.dimensions['length_ft']}\'-{self.dimensions['length_in']}\""
            width = f"{self.dimensions['width_ft']}\'-{self.dimensions['width_in']}\""
            return f"{length} x {width}"
        else:
            return None


    def __str__(self):
        """Informal string representation of object.

        Parameters:
            None

        Returns:
            str: name, number of object and associated building name
        """

        string = f"{self.story.building.name}, {self.story.name},"
        if self.number:
            string += f"{self.number},"
        string += f" {self.name}"

        return string
