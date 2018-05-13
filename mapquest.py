import json
import urllib.parse
import urllib.request


API_KEY = "n8W4BMJzJNpZMatMviGbfF7eK8VIjtsA"
BASE_URL = "http://open.mapquestapi.com"


def build_route_url(locations: list) -> str:
    """ Builds route URL to open based on inputs """
    query_parameters = [("key", API_KEY), ("from", locations[0])]
    for index in range(len(locations)):
        if index != 0:
            query_parameters.append(("to", locations[index]))

    return str(BASE_URL + "/directions/v2/route?" + urllib.parse.urlencode(query_parameters))


def build_elevation_url(lat: float, long: float) -> str:
    """ Builds elevation URL to open based on inputs """
    query_parameters = [("key", API_KEY), ("unit", "f"),
                        ("latLngCollection", "{}, {}".format(lat, long))]

    return str(BASE_URL + "/elevation/v1/profile?" + urllib.parse.urlencode(query_parameters))


def get_result(url: str) -> 'json':
    """ Takes a URL and returns a Python object representing the parsed JSON response. """
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding='utf-8')
        return json.loads(json_text)
    except:
        print("MAPQUEST ERROR")
    finally:
        if response is not None:
            response.close()


