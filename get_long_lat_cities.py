from geopy.geocoders import Nominatim
import pandas as pd


# initialize the geolocator
geolocator = Nominatim(user_agent="TravellingSalesManEu")


def get_long_lat_dataFrame(cities: list = None) -> pd.DataFrame:
    """
    Get the latitude and longitude of a list of cities and return a pandas DataFrame.

    Parameters:
    cities (list, optional): A list of city names. If not provided or empty, a default list of European cities is used.

    Returns:
    pd.DataFrame: A DataFrame containing the city names along with their corresponding latitude and longitude.

    Example:
    >>> get_long_lat_dataFrame(["New York", "Los Angeles"])
           City   latitude  longitude
    0  New York  40.712776 -74.005974
    1  Los Angeles  34.052235 -118.243683
    """
    # if the list of cities is empty, use a default list of cities
    if cities is None or len(cities) == 0:
        cities:list= [
            "Brussels",
            "Paris",
            "Madrid",
            "Frankfurt",
            "Poznań",
            "Copenhagen",
            "Kraków",
            "Berlin",
            "Vienna",
            "Rome",
            "Amsterdam",
            "Lisbon",
            "Stockholm",
            "Oslo",
            "Helsinki",
            "Vilnius",
            "Dublin",
            "Warsaw",
            "Budapest",
            "Prague",
        ]
    # initialize an empty list to store the cities and their latitude and longitude
    cities_list: list = []
    # loop through the list of cities and get the latitude and longitude
    for city in cities:
        location = geolocator.geocode(city)
        # print(city, location.latitude, location.longitude)
        new_city:dict = {
            "City": city,
            "latitude": location.latitude,
            "longitude": location.longitude,
        }
        cities_list.append(new_city)

    city_df:pd.DataFrame = pd.DataFrame(data=cities_list, columns=["City", "latitude", "longitude"])
    return city_df
