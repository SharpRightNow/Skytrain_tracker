# import packages
import csv
import time

route_columns_to_keep = ["route_long_name",
                         "route_short_name",
                         "route_id",]
trip_columns_to_keep = ["route_id",
                        "trip_id",
                        "direction_id",
                        "trip_headsign",
                        "shape_id",
                        "service_id",]
stop_time_columns_to_keep = ["trip_id",
                             "arrival_time",
                             "departure_time",
                             "stop_id",
                             "stop_sequence",
                             "shape_dist_traveled",]

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
    route_ids_set = set(route_ids)  # Convert list to set for faster lookup

    with open("GTFS data/routes.txt", "r") as routes_file:

        routes_read = csv.DictReader(routes_file)
        headers = routes_read.fieldnames

        for route in routes_read:
            if route["route_id"] in route_ids_set:
                for key in headers:
                    if key not in columns_to_keep:
                        del route[key]
                tracked_routes.append(route)

    return tracked_routes


def get_clean_trip_data(route_ids, columns_to_keep):
    """Takes in a list of route ids, and a list of desired data about the trips, and
    returns a list of all specified trips as dicts, each with a description of
    the data, then the data."""

    route_ids_set = set(route_ids)  # Convert list to set for faster lookup
    tracked_trips = []

    with open("GTFS data/trips.txt", "r") as trips_file:

        trips_read = csv.DictReader(trips_file)
        headers = trips_read.fieldnames

        for trip in trips_read:
            if trip["route_id"] in route_ids_set:
                for key in headers:
                    if key not in columns_to_keep:
                        del trip[key]
                tracked_trips.append(trip)

    return tracked_trips


def get_clean_stop_times_data(trip_ids, columns_to_keep):
    """Takes in a list of trip ids, and a list of desired data about the stops, and
    returns a list of all specified stops as dicts, each with a description of
    the data, then the data."""

    trip_ids_set = set(trip_ids)  # Convert list to set for faster lookup

    tracked_stops = []

    with open("GTFS data/stop_times.txt", "r") as stop_times_file:

        stop_times_read = csv.DictReader(stop_times_file)
        headers = stop_times_read.fieldnames

        for stop_time in stop_times_read:
            if stop_time["trip_id"] in trip_ids_set:
                for key in headers:
                    if key not in columns_to_keep:
                        del stop_time[key]
                tracked_stops.append(stop_time)

    return tracked_stops


def get_clean_stops_data(stop_ids, columns_to_keep):
    """Takes in a list of stop ids, and a list of desired data about the stops, and
    returns a list of all specified stops as dicts, each with a description of
    the data, then the data."""

    stop_ids_set = set(stop_ids)  # Convert list to set for faster lookup

    tracked_stops = []

    with open("GTFS data/stops.txt", "r") as stops_file:

        stops_read = csv.DictReader(stops_file)
        headers = stops_read.fieldnames

        for stop in stops_read:
            if stop["stop_id"] in stop_ids_set:
                for key in headers:
                    if key not in columns_to_keep:
                        del stop[key]
                tracked_stops.append(stop)

    return tracked_stops


def get_clean_data(ids, columns_to_keep, data_type):

    # Supported data types (file name) and the id we're filtering with
    supported_data_types = {"routes": "route_id",
                            "trips": "route_id",
                            "stop_times": "stop_id",
                            "stops": "stop_id"}

    if data_type not in supported_data_types:
        raise ValueError(
            f"Unsupported data type: {data_type}. Supported types are: {', '.join(supported_data_types.keys())}")

    id_key = supported_data_types[data_type]
    ids_set = set(ids)  # Convert list to set for faster lookup

    tracked_data = []

    with open(f"GTFS data/{data_type}.txt", "r") as file:

        read = csv.DictReader(file)
        headers = read.fieldnames

        for row in read:
            if row[id_key] in ids_set:  # Never returns true
                for key in headers:
                    if key not in columns_to_keep:
                        del row[key]
                tracked_data.append(row)
    return tracked_data


# print(get_clean_trip_data(tracked_route_ids, trip_columns_to_keep))
print(get_clean_data(tracked_route_ids, route_columns_to_keep, "routes"))
