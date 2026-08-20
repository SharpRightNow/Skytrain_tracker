import data_parser
import vehicle_class as vehicle
import sys

# create vehicle objects

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
tracked_route_ids = ["30053",  # Expo line
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

routes = data_parser.get_clean_data(
    tracked_route_ids, route_columns_to_keep, "routes")

# print(routes)

trips = data_parser.get_clean_data(
    tracked_route_ids, trip_columns_to_keep, "trips")

# print(trips)

print(sys.getsizeof(routes), sys.getsizeof(trips), )
# for trip in trips:
#     stop_times = data_parser.get_clean_data()

# print(trips)

# [vehicle(1, trip, ) for trip in trips]

# for trip in trips:
#     vehicle()

# trips = {route:route[] for route in routes}
