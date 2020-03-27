import csv
import building as bld
# from building import Building, Story, Space (either one is fine)

# LECTURE 18 Objectives

# Objectives
# 1. Develop understanding of class inheritance and class composition
# 2. Import and use a custom module (building.py)
# 3. Use super() to call the supertype's __init__() method
# 4. Work with supertypes and subtypes (e.g. parent/child classes)
# 5. Read/write files


def add_stories_and_spaces(building, data):
    """Add stories and spaces to building from provided data.

    Parameters:
        building (Building): target building
        data (list): list of stories and spaces to add to building

    Returns:
        building: updated building

    """

    # Get unique story names
    story_names = get_story_names(building, data)

    # Add building stories and spaces
    for story_name in story_names:
        story = bld.Story(story_name, building)
        for row in data:
            if row[0] == building.name and row[2] == story_name:
                dimensions = {
                    'length_ft': row[3], 'length_in': row[4],
                    'width_ft': row[5], 'width_in': row[6]
                    }
                space = bld.Space(row[1], dimensions, story)
                story.add_space(space)
        building.add_story(story)

    return building


def get_story_names(building, data):
    """Return list of unique story names from provided data.

    Parameters:
        building (Building): target building
        data (list): list of stories and spaces

    Returns:
        list: sequence of unique story names

    """

    names = []
    for row in data:
        if row[0].lower() == building.name.lower() and row[2] not in names:
            names.append(row[2])

    return names


def read_csv(path, delimiter=','):
    """Accepts a path, creates a file object, and returns a list of
    the file contents, line by line. Utilizes built-in enumerate()
    to filter out headers line.

    Parameters:
        path (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested lists representing the file contents
     """

    with open(path, 'r', newline='', encoding='utf-8') as csv_file:
        data = []
        reader = csv.reader(csv_file, delimiter=delimiter)
        for i, line in enumerate(reader):
            if i > 0:
                data.append(line)

        return data


def write_file(path, data):
    """Accepts a path, creates a file object, and returns a list of
    dictionaries that represent the row values.

    Parameters:
        path (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(path, 'w', newline='', encoding='utf-8') as file_obj:
        # file_obj.write(data)
        # file_obj.writelines(data)

        for row in data:
            file_obj.write(row)


def main():
    """Entry point of program.

    Parameters:
        None

    Returns:
        None
    """

    # 1.0 GET CSV DATA
    path = 'wright_buildings.csv'
    data = read_csv(path)

    print(f"\n {data}")

    # 1.1 CREATE BUILDING
    # Import building classes above

    # Fallingwater, Frank Lloyd Wright (1935)
    # 1491 Mill Run Rd, Mill Run, PA 15464
    # https://fallingwater.org/

    building = bld.Building('Fallingwater', 39.906431, -79.467943)

    # 1.2 PRINT BUILDING TYPE IRI AND ID

    print(f"\n{building.name}\niri = {building.type_iri}\nid = {building.id_}\n")

    # 1.2 SUBCLASS CHECK
    print(f"Building subclass of Zone = {issubclass(bld.Building, bld.Zone)}\n")

    # 1.3 INSTANCE CHECK
    print(f"building instance of Building = {isinstance(building, bld.Building)}\n")

    # 1.4 ADD FLOORS AND ROOMS FROM CSV DATA
    building = add_stories_and_spaces(building, data)

    # 1.5 UNCOMMENT COUNT NUM ROOMS PER FLOOR
    for story in building.stories:
        print(f"{story.name} rooms = {story.num_spaces()}")

    print('\n') # padding

    # 1.6 PRINT TO SCREEN BUILDING FLOORS AND ROOMS
    print(building)

    # 1.7 WRITE BUILDING TO FILE
    path = f"{building.name.replace(' ', '_').lower()}.txt" # dynamic file naming
    write_file(path, building.__str__())

    # 2.0 PROCESS OTHER BUILDING INFO

    # Meyer May House, Frank Lloyd Wright (1908-09)
    # Wright's "Prairie School era Masterpiece"
    # 450 Madison Ave SE, Grand Rapids, MI 49503
    # https://meyermayhouse.steelcase.com/

    building = bld.Building('Meyer May House', 42.954387, -85.658782)
    building = add_stories_and_spaces(building, data)
    path = f"{building.name.replace(' ', '_').lower()}.txt"
    write_file(path, building.__str__())

    # Palmer House, Frank Lloyd Wright (1950)
    # 227 Orchard Hills Dr, Ann Arbor, MI 48104
    # http://flwpalmerhouse.com/

    building = bld.Building('Palmer House', 42.278714, -83.715812)
    building = add_stories_and_spaces(building, data)
    path = f"{building.name.replace(' ', '_').lower()}.txt"
    # write_file(path, building.__str__())

if __name__ == '__main__':
    main()