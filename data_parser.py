# import packages
import csv
import time
import sys

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


def get_clean_data(ids, columns_to_keep, data_type):

    # Supported data types (file name) and the id we're filtering with
    supported_data_types = {"routes": ["route_id"],
                            "trips": ["route_id"],
                            "stop_times": ["stop_id"],
                            "stops": ["stop_id"]}

    if data_type not in supported_data_types:
        raise ValueError(
            f"Unsupported data type: {data_type}. Supported types are: {', '.join(supported_data_types.keys())}")

    filter_id = supported_data_types[data_type][0]
    ids_set = set(ids)  # Convert list to set for faster lookup
    columns_to_keep_set = set(columns_to_keep)
    columns_to_keep_set.discard(filter_id)

    tracked_data = []

    with open(f"GTFS data/{data_type}.txt", "r") as file:

        file_read = csv.DictReader(file)
        headers = file_read.fieldnames

        for row in file_read:
            id = row[filter_id]
            if id in ids_set:
                tracked_data.append(
                    {id: {key: row[key] for key in headers if key in columns_to_keep_set}})
    return tracked_data
