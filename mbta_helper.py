import urllib.request
import json
from pprint import pprint


MAPQUEST_API_KEY = '612GO4nIe6OIAMQFEfA2knOE2zBYsqKU'
MBTA_KEY = '1c50c8e2efb94d1d8c36d530adfe68c2'


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    responses_data = get_json(url)
    result = (responses_data['results'][0]['locations'][0]['latLng']['lat'],
              responses_data['results'][0]['locations'][0]['latLng']['lng'])
    return result


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    #/Stop/ApiWeb_StopController_index for URL
    See https://api-v3.mbta.com/docs/swagger/index.html
    formatting requirements for the 'GET /stops' API.
    """
    MBTA_URL = f"https://api-v3.mbta.com/stops?api_key={MBTA_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    responses_data =get_json(MBTA_URL)
    return (responses_data['data'][0]["attributes"]['name'], responses_data['data'][0]["attributes"]['wheelchair_boarding'])


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    latitude, longitude = get_lat_long(place_name)
    return get_nearest_station(latitude, longitude)


def main():
    """
    You can test all the functions here
    """
    print(find_stop_near("boston"))


if __name__ == '__main__':
    main()
