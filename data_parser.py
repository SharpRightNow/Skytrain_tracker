# import packages
import csv

route_columns_to_keep = ["route_long_name",
                         "route_short_name",
                         "route_id",]
trip_columns_to_keep = ["route_id",
                        "trip_id",
                        "direction_id",
                        "block_id",
                        "trip_headsign",
                        "shape_id",
                        "service_id",]


tracked_route_ids = [
    "30053",  # Expo line
    "30052",  # Millennium line
    "13686",  # Canada line
    "6641",  # Broadway B-Line
    "37808",  # King George Blvd (R1)
    "38311",  # Marine Drive (R2)
    "37809",  # Lougheed Hwy (R3)
    "37810",  # 41st Avenue (R4)
    "37807",  # Hastings St (R5)
    "46604",  # Scott Road (R6)
]

"""tracked_routes_names = [["Expo Line", ""],
                        ["Millennium Line", ""],
                        ["Canada Line", ""],
                        ["Broadway B-Line", ""],
                        ["King George Blvd", "R1"],  # R1
                        ["Marine Drive", "R2"],  # R2
                        ["Lougheed Hwy", "R3"],  # R3
                        ["41st Avenue", "R4"],  # R4
                        ["Hastings St", "R5"],  # R5
                        ["Scott Road", "R6"],  # R6
                        ]"""


def get_clean_route_data(route_ids, columns_to_keep):
    """Takes in a list of route ids, and a list of desired data about those routes and
    returns a list of the specified routes as dicts, each with a description of the 
    data, then the data."""

    tracked_routes = []

    with open("GTFS data/routes.txt", "r") as routes_file:

        routes_read = csv.DictReader(routes_file)
        headers = routes_read.fieldnames

        for route in routes_read:
            for key in headers:
                if key not in columns_to_keep:
                    del route[key]

            if route["route_id"] in route_ids:
                tracked_routes.append(route)

    return tracked_routes


def get_clean_trip_data(route_ids, columns_to_keep):
    """Takes in a list of route ids, and a list of desired data about those trips, and
    returns a list of all specified trips as dicts, each with a description of 
    the data, then the data."""

    tracked_trips = []

    with open("GTFS data/trips.txt", "r") as trips_file:

        trips_read = csv.DictReader(trips_file)
        headers = trips_read.fieldnames

        for trip in trips_read:
            for key in headers:
                if key not in columns_to_keep:
                    del trip[key]

            if trip["route_id"] in route_ids:
                tracked_trips.append(trip)

    return tracked_trips


data = get_clean_trip_data(tracked_route_ids, trip_columns_to_keep)

for i in data:
    for n in data:
        if i['route_id'] == n['route_id'] and i['direction_id'] == n['direction_id']:
            if i["shape_id"] != n["shape_id"]:
                print("shapes dont match on trip " +
                      i["trip_id"] + " and trip " + n["trip_id"])
