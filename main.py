import heapq
import datetime

import data_parser
import vehicle_class
import stop_class

# Create a priority queue for vehicles, using a heap
q = []

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

tracked_routes_names = [["Expo Line", ""],
                        ["Millennium Line", ""],
                        ["Canada Line", ""],
                        ["Broadway B-Line", ""],
                        ["King George Blvd", "R1"],  # R1
                        ["Marine Drive", "R2"],  # R2
                        ["Lougheed Hwy", "R3"],  # R3
                        ["41st Avenue", "R4"],  # R4
                        ["Hastings St", "R5"],  # R5
                        ["Scott Road", "R6"],  # R6
                        ]

# route_ids = [data_parser.get_route_ids(route[0])
#              for route in tracked_routes_names]
# trip_ids = {route_id: data_parser.get_trip_ids(
#     route_id) for route_id in route_ids}

routes = {route_id: (route_long_name, route_short_name, route_color)}
trips = {route_id: (trip_id_1, trip_id_2, trip_id_3)}
stops = {trip_id: {stop_id: (arrival_time, departure_time, stop_sequence)},
         stop_id_2: (arrival_time_2, departure_time_2, stop_sequence_2),
         stop_id_3: (arrival_time_3, departure_time_3, stop_sequence_3)}

stops2 = {trip_id: [stop_class.stop(stop_id, arrival_time, departure_time, stop_sequence),
                    stop_class.stop(stop_id_2, arrival_time_2,
                                    departure_time_2, stop_sequence_2),
                    stop_class.stop(stop_id_3, arrival_time_3, departure_time_3, stop_sequence_3)]}

# GTFS data to be held in memory like this:
# route
#     trip
#         stops
#             stop_times


# Stops pseudo code
# read into mem
# grab only relevent lines
# put each line into a class
# put each class into one list
# sort list by stop_seaquence
# put list into a dict with trip_id as key


for i in range(5):
    # Create a vehicle object with dummy data
    v = vehicle_class.vehicle(route=f"Route {i}", trip=f"Trip {i}",
                              stops=[], stop_times=[], start_time=datetime.datetime.now())

    # Add the vehicle to the priority queue with its next light time as the priority
    heapq.heappush(q, v)

# Time speed up can be done by using a sort of delta time,
# and multiplying it by the time speed up/slow down factor,
# normal/realtime can just be a factor of 1

""""""

while True:
    vehicle_to_update = []
    lights_to_update = []

    # Get current time
    current_time = datetime.datetime.now()

    # Check queue for vehicles to update
    while q and q[0].next_light_time <= current_time:
        vehicle_to_update.append(heapq.heappop(q))

    # For each vehicle to be updated:
    for vehicle in vehicle_to_update:
        lights_to_update.append((vehicle.get_next_light(), 1))
        lights_to_update.append((vehicle.get_current_light(), 0))

        vehicle.next_light()

        heapq.heappush(q, vehicle)

    # TODO: Add lights changing code
