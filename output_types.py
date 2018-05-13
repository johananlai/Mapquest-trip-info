import mapquest


class Steps:

    def __init__(self, locations: list):
        self._locations = locations

    def print_info(self) -> None:
        """ Prints step-by-step directions for every location """
        try:
            route_url = mapquest.build_route_url(self._locations)
            result = mapquest.get_result(route_url)

            if int(result["route"]["routeError"]["errorCode"]) == 0:
                print("NO ROUTE FOUND")
            else:
                print("DIRECTIONS")
                for leg in result["route"]["legs"]:
                    for maneuver in leg["maneuvers"]:
                        print(maneuver["narrative"])
        except:
            print("MAPQUEST ERROR")
        print()


class Totaldistance:

    def __init__(self, locations: list):
        self._locations = locations

    def print_info(self) -> None:
        """ Prints total distance total length of trip """
        try:
            route_url = mapquest.build_route_url(self._locations)
            result = mapquest.get_result(route_url)

            if int(result["route"]["routeError"]["errorCode"]) == 0:
                print("NO ROUTE FOUND")
            else:
                print("TOTAL DISTANCE: {:d} miles".format(round(result["route"]["distance"])))
        except:
            print("MAPQUEST ERROR")
        print()


class Totaltime:

    def __init__(self, locations: list):
        self._locations = locations

    def print_info(self) -> None:
        """ Prints total time for total length of trip """
        try:
            route_url = mapquest.build_route_url(self._locations)
            result = mapquest.get_result(route_url)

            if int(result["route"]["routeError"]["errorCode"]) == 0:
                print("NO ROUTE FOUND")
            else:
                print("TOTAL TIME: {:d} minutes".format(round(result["route"]["time"]/60.0)))
        except:
            print("MAPQUEST ERROR")
        print()


class Latlong:

    def __init__(self, locations: list):
        self._locations = locations

    def print_info(self) -> None:
        """ Prints step-by-step directions for every location """
        try:
            route_url = mapquest.build_route_url(self._locations)
            result = mapquest.get_result(route_url)

            if int(result["route"]["routeError"]["errorCode"]) == 0:
                print("NO ROUTE FOUND")
            else:
                print("LATLONGS")
                for location in result["route"]["locations"]:
                    lat = float(location["latLng"]["lat"])
                    long = float(location["latLng"]["lng"])
                    if lat < 0.0:
                        lat *= -1.0
                        lat = str(round(lat, 2)) + "S"
                    else:
                        lat = str(round(lat, 2)) + "N"
                    if long < 0.0:
                        long *= -1.0
                        long = str(round(long, 2)) + "W"
                    else:
                        long = str(round(long, 2)) + "E"
                    print("{:s} {:s}".format(lat, long))
        except:
            print("MAPQUEST ERROR")
        print()


class Elevation:

    def __init__(self, locations: list):
        self._locations = locations

    def print_info(self) -> None:
        """ Prints elevations of each location """
        route_url = mapquest.build_route_url(self._locations)
        result = mapquest.get_result(route_url)

        print("ELEVATIONS")
        for location in result["route"]["locations"]:
            lat = float(location["latLng"]["lat"])
            long = float(location["latLng"]["lng"])

            elevation_url = mapquest.build_elevation_url(lat, long)
            elevation_result = mapquest.get_result(elevation_url)

            elevation = round(elevation_result["elevationProfile"][0]["height"])
            print(elevation)
        print()
