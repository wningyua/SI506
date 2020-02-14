# Lecture 11 Exercise Objectives

# 01. Break problems down into sub problems
# 02. Write functions that count, format, and get data
# 03. Work with a list of dictionaries
# 04. Implement accumulator pattern
# 05. Write for loops and conditional statements to filter data
# 06. Perform true value test
# 07. Write expressions using a membership operator (in, not in)
# 08. Read function Docstrings (spec/contract)
# 09. Control execution path from main() function


def count_seats_by_country(tour_dates, country=None):
    """
    Return count of tour date seats to fill filtered by
    country. If no country is provided by caller return
    all tour dates seats to fill. If wrong country is
    provided return 0.

    Parameters:
        tour_dates (list): list of tour dates
        country (str): filter string

    Returns:
        int: filtered count of seats to fill.
    """

    seats = 0
    for tour_date in tour_dates:
        if not country:
            seats += tour_date["seating"]
        elif tour_date['country'] == country:
            seats += tour_date["seating"]
        else:
            continue
    return seats


def count_tour_dates_by_location(tour_dates, location='venue'):
    """Return dictionary of tour date counts by location. Each
    filtered tour_date location provides a key for the new
    dictionary to be returned while the associated tour date count
    provides the value.

    Parameters:
        tour_dates (list): list tour date dictionaries.
        location (str): 'venue' (default), 'city', 'country'.

    Returns:
        dict: a dictionary of location (key) tour date counts (value).
    """

    counts = {}
    for tour_date in tour_dates:
        for key, value in tour_date.items():
            if key ==location:
                if value in counts.keys():
                    counts[value] +=1
                else:
                    counts[value] = 1
    return counts



def format_location(event, location='venue'):
    """Return formatted event location string. Optional location
    parameter determines geographical scope of the location string
    to  be returned.

    Location values accepted:
    'venue': '<venue>, <city>, <country>' (default)
    'city': <city>, <country>'
    'country': <country>'

    Parameters:
        event (list): list of event attributes
        location (str): determines geographical scope of location

    Returns:
        str: venue location as scoped by location argument
    """
    if location == 'city':
        return f"{event['city']}, {event['country']}"
    elif location == 'country':
        return event['country']
    else: 
        return f"{event['venue']}, {event['city']}, {event['country']}"



def get_locations(tour_dates, location='venue'):
    """Returns list of event locations, filtering out duplicates.
    Format location strings by calling format_event_location() passing
    location and string constant that sets the location scope (i.e.,
    building, city, country).

    Parameters:
        tour_dates (list): list of events
        locations (str): optional string that determines location scope.

    Returns:
        list: list of formatted event locations
    """
    locations = []
    for tour_date in tour_dates:
        place = format_location(tour_date, location)
        if place not in locations:
            locations.append(place)
    return locations
    


def get_venues_by_seating(tour_dates, min_seats, max_seats=None):
    """Return a list of venue dictionaries filtered by available
    seating. Both min and max seating values may be provided to
    identify a range of venues that meet the min/max seating
    criteria. If no max_seats value is provided, the min_seats
    value will also serve as the max_seats value.

    Both band and date key/value pairs are excluded from the returned
    dictionary. This is done to facilitate the filtering out of
    duplicate dictionaries in the returned list.

    Parameters:
        tour_dates (list): list of events.
        min_seats (int): minimum number of available seats.
        max_seats (int): maximum number of available seats.

    Returns:
        dict: a dictionary of filtered venues.
    """
    venues = []
    if not max_seats:
        max_seats = min_seats
    for tour_date in tour_dates:
        venue = {
            'venue': tour_date['venue'],
            'city': tour_date['city'],
            'country': tour_date['country'],
            'seating': tour_date['seating']
        }

        if (venue not in venues and min_seats <= venue['seating'] <= max_seats):
            venues.append(venue)

    return venues


def main():
    """Entry point for program.

    Parameters:
        None

    Returns:
        None
    """

    tour_dates = [
        {
            'band': 'JLCO',
            'date': 'February 10, 2020',
            'venue': 'DR Koncerthuset',
            'city': 'Copenhagen',
            'country': 'Denmark',
            'seating': 1800
        },
        {
            'band': 'JLCO',
            'date': 'February 11, 2020',
            'venue': 'Musikkens Hus',
            'city': 'Aalborg',
            'country': 'Denmark',
            'seating': 1293
        },
        {
            'band': 'JLCO',
            'date': 'February 12, 2020',
            'venue': 'Elbphilharmonie',
            'city': 'Hamburg',
            'country': 'Germany',
            'seating': 2100
        },
        {
            'band': 'JLCO',
            'date': 'February 13, 2020',
            'venue': 'Konzerthaus Dortmund',
            'city': 'Dortmund',
            'country': 'Germany',
            'seating': 1500
        },
        {
            'band': 'JLCO',
            'date': 'February 14, 2020',
            'venue': 'Philharmonie Luxembourg',
            'city': 'Luxembourg City',
            'country': 'Luxembourg',
            'seating': 1500
        },
        {
            'band': 'JLCO',
            'date': 'February 16, 2020',
            'venue': 'HET Concertgebouw',
            'city': 'Amsterdam',
            'country': 'Netherlands',
            'seating': 1974
        },
        {
            'band': 'JLCO',
            'date': 'February 17, 2020',
            'venue': 'HET Concertgebouw',
            'city': 'Amsterdam',
            'country': 'Netherlands',
            'seating': 1974
        },
        {
            'band': 'JLCO',
            'date': 'February 18, 2020',
            'venue': 'Henry Le Boeuf Hall - BOZAR',
            'city': 'Brussels',
            'country': 'Belgium',
            'seating': 700
        },
        {
            'band': 'JLCO',
            'date': 'February 19, 2020',
            'venue': 'Henry Le Boeuf Hall - BOZAR',
            'city': 'Brussels',
            'country': 'Belgium',
            'seating': 700
        },
        {
            'band': 'JLCO',
            'date': 'February 22, 2020',
            'venue': 'National Forum of Music',
            'city': 'Wrocław',
            'country': 'Poland',
            'seating': 1800
        },
        {
            'band': 'JLCO',
            'date': 'February 23, 2020',
            'venue': 'National Polish Radio Symphony Orchestra',
            'city': 'Katowice',
            'country': 'Poland',
            'seating': 1800
        },
        {
            'band': 'JLCO',
            'date': 'February 24, 2020',
            'venue': 'Wiener Konzerthaus',
            'city': 'Vienna',
            'country': 'Austria',
            'seating': 1840
        },
        {
            'band': 'JLCO',
            'date': 'February 25, 2020',
            'venue': 'Wiener Konzerthaus',
            'city': 'Vienna',
            'country': 'Austria',
            'seating': 1840
        },
        {
            'band': 'JLCO',
            'date': 'February 26, 2020',
            'venue': 'Wiener Konzerthaus',
            'city': 'Vienna',
            'country': 'Austria',
            'seating': 1840
        },
        {
            'band': 'JLCO',
            'date': 'February 28, 2020',
            'venue': 'Palau de la Música Catalana',
            'city': 'Barcelona',
            'country': 'Spain',
            'seating': 538
        }
    ]

    # Count tour dates
    count = len(tour_dates)

    print(f"\ntour_dates count = {count}\n")


    # 1.0 Warmup

    # Get 1st event: country
    country = tour_dates[0]['country']

    print(f"1st country visted = {country}\n")


    # Get list of Vienna tour dates
    vienna_dates = tour_dates[-4:-2]
    print(f"Vienna dates = {vienna_dates}\n")


    # 2.0 EXERCISE

    # Write function that returns tour locations (venue, city, or country).
    # Pass in optional filter value (see Docstring).
    # Return formatted string value (see Docstring).


    # Tour countries (country)
    countries = get_locations(tour_dates, 'country')

    print(f"Tour Countries (n={len(countries)})")
    for country in countries:
        print(country)


    # Tour cities (<city>, <country>)
    cities = get_locations(tour_dates, 'city')

    print(f"\nTour Cities (n={len(cities)})")
    for city in cities:
        print(city)


    # Tour venues (<venue>, <city>, <country>)
    venues = get_locations(tour_dates)

    print(f"\nTour Venues (n={len(venues)})")
    for venue in venues:
        print(venue)


    # 3.0 EXERCISE

    # Write function that returns 'seats to fill' counts by country.
    # Pass in country string as optional filter value (see Docstring).
    # Default parameter country=None (return count all countries)
    # Return seating count filtered by country.

    # All tour dates seats to fill
    seat_count = count_seats_by_country(tour_dates)

    print(f"\nAll venues seat_count = {seat_count}\n")


    # Austrian tour dates seats to fill
    seat_count = count_seats_by_country(tour_dates, 'Austria')

    print(f"Austrian venues seat_count = {seat_count}\n")


    # French tour dates seats to fill
    seat_count = count_seats_by_country(tour_dates, 'France')

    print(f"French venues seat_count = {seat_count}\n")


    # 4.0 EXERCISE

    # Write function to return concert venues by seating count.
    # Allow caller to provide min and max seating values (see Docstring).
    # Return list of 'reshaped' venue dictionaries (see Doctring)

    # Venues featuring between 500 and 1000 seats.
    venue_seating = get_venues_by_seating(tour_dates, 500, 1000)

    print(f"\nvenue_seating = {venue_seating}\n")


    # Venues featuring exactly 1840 seats.
    venue_seating = get_venues_by_seating(tour_dates, 1840)

    print(f"venue_seating = {venue_seating}\n")


    # 5.0 EXERCISE

    # Write function that provides counts of tour dates by location.
    # Pass in optional filter value (see Docstring).
    # Return dictionary using location value as key (see Docstring).

    # Count tour dates by venue
    counts = count_tour_dates_by_location(tour_dates, 'city')

    print('\nTour Dates by City')
    for key in sorted(counts.keys()):
        print(f"{key}: {counts[key]}")


    # Count tour dates by country
    counts = count_tour_dates_by_location(tour_dates, 'country')

    print('\nTour Dates by Country')
    for key in sorted(counts.keys()):
        print(f"{key}: {counts[key]}")

    print('\n') # padding

if __name__ == '__main__':
    main()
