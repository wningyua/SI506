import requests
import sw_utilities as utils
from sw_entities import Planet, INT_PROPS, LIST_PROPS


# LECTURE 23 Exercise

# Objectives
# 1. Write list comprehensions
# 2. Write dictionary comprehensions
# 3. Work with class instances
# 3. Work with custom modules

# CONSTANTS
ENDPOINT = 'https://swapi.py4e.com/api'

def main():
    """Entry point for program. Orchestrates workflow."""

    # 1.0 RETRIEVE DATA SET (SWAPI PLANETS)
    filepath = 'swapi_planets.json'
    swapi_planets = utils.read_json(filepath) # note module reference

    print(f"\nPlanet count = {len(swapi_planets)}\n")


    # 2.0 LIST COMPREHENSION REVIEW
    # Task: Identity planets with a tropical climate

    # 2.0.1 for loop
    tropical = []
    for p in swapi_planets:
        if "tropical" in p["climate"]:
            tropical.append(p)

    # TODO WRITE FOR LOOP

    print(f"\nFor: Planets w/Tropical climate = {len(tropical)}\n")

    # 2.0.2 list comprehension
    # format: [<expression> for <element> in <sequence> if <condition>]

    tropical.clear()
    tropical = [p for p in swapi_planets if "tropical" in p["climate"]] # FIX ME

    print(f"\nComp: Planets w/Tropical climate  = {len(tropical)}\n")


    # 2.1 FILTER KEY/VALUES (DICTIONARY/LIST COMPREHENSION)
    # Work with planet dictionaries
    # Exclude: films, created, and edited key/value pairs
    # Call util.filter_data(data, filter_keys)

    # Tasks
    # 1. Write a dict comprehension in utils.filter_data(data, filter_keys)
    # 2. Write list comprehension assigning filtered planet to planets list

    # 2.1.1 for loop
    planets = []
    for planet in swapi_planets:
        planet_filtered = utils.filter_data(planet, Planet.KEYS)
        planets.append(planet_filtered)

    # UNCOMMENT
    print(f"\nFor: Filtered Planet = {planets[0]}\n") # 1st record only

    # 2.1.2 list comprehension
    planets.clear() # reset
    planets = [utils.filter_data(planet, Planet.KEYS) for planet in swapi_planets ] # FIX ME

    print(f"\nComp: Filtered Planet = {planets[0]}\n") # 1st record only


    # 2.2 CLASS INSTANCE VARIABLE FILTERING
    # Work with Planet objects
    # Initialize class instance with dict values

    # 2.2.1 for loop
    planet_objs = []
    for planet in swapi_planets:
        obj = Planet(
            planet['name'],
            planet['url'],
            planet['rotation_period'],
            planet['orbital_period'],
            planet['diameter'],
            planet['climate'],
            planet['gravity'],
            planet['terrain'],
            planet['surface_water'],
            planet['population']
        )
        planet_objs.append(obj)

    print(f"\nFor: Planet objs = {planet_objs[0].jsonable()}\n")

    # 2.2.2 list comprehension
    planet_objs.clear()
    planet_objs = [Planet(
            planet['name'],
            planet['url'],
            planet['rotation_period'],
            planet['orbital_period'],
            planet['diameter'],
            planet['climate'],
            planet['gravity'],
            planet['terrain'],
            planet['surface_water'],
            planet['population']
        ) 
        for planet in swapi_planets] # FIX ME

    print(f"\nComp: Planet objs = {planet_objs[0].jsonable()}\n")


    # 2.3 CONVERT STRINGS TO INT AND LIST
    # Work with planet dictionaries
    # Check if key in tuple of convert 'friendly' keys; call utility function

    # 2.3.1 for loop
    # TODO WRITE FOR LOOP
    planet_vals = []
    for planet in planets:
        for key, val in planet.items():
            if key in INT_PROPS:
                planet[key] = utils.convert_string_to_int(val)
            elif key in LIST_PROPS:
                planet[key] = utils.convert_string_to_list(val, ", ")
            else:
                planet[key] = val
        planet_vals.append(planet)


    print(f"\nFor: Planet ints = {planet_vals[0]}\n") # 1st record only

    # 2.3.2 list comp / dict comp
    # elif not permitted (nested if might work)
    planet_vals.clear()
    # planet_vals = [
    #     {
    #         key: utils.convert_string_to_int(val)
    #         if key in INT_PROPS
    #         utils.convert_string_to_list(val)
    #         elif key in LIST_PROPS
    #         else val
    #         for key, val in planet.items()
    #     }
    #     for planet in planets
    # ]

    # UNCOMMENT Workaround
    def converter(key, val):
    #     """TODO"""

        if key in INT_PROPS:
            return utils.convert_string_to_int(val)
        elif key in LIST_PROPS:
            return utils.convert_string_to_list(val, ', ')
        else:
            return val

    planet_vals = [
        {key: converter(key, val) for key, val in planet.items()}
        for planet in planets
        ] # FIX ME

    print(f"\nComp: Planet ints = {planet_vals[0]}\n") # 1st record only


    # 2.4 CONVERT OBJECT INSTANCE VARIABLE STRINGS TO INT AND LIST
    # Work Planet objects

    # 2.4.1 for loop (update instance variables)

    # UNCOMMENT
    for planet in planet_objs:
        for key, val in planet.__dict__.items():
            setattr(planet, key, converter(key, val))

    print(f"\n For: Planet rotation period = {planet_objs[0].rotation_period}\n")

    # 2.4.2 list comp (update instance variables)
    # format: [<expression> for <element> in <sequence> for <k,v> in dict.items()]

    # TODO WRITE LIST COMPREHENSION
    [
        setattr(planet, key, converter(key,val))
        for planet in planet_objs
        for key, val in planet.__dict__.items()
    ]
    print(f"\n Comp: Planet rotation period = {planet_objs[0].rotation_period}\n")


if __name__ == '__main__':
    main()