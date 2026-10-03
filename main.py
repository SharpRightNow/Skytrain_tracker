import heapq
import datetime
import csv

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

tracked_routes_names = ("Expo Line",
                        "Millennium Line",
                        "Canada Line",
                        "Broadway B-Line",
                        "King George Blvd",  # R1
                        "Marine Drive",  # R2
                        "Lougheed Hwy",  # R3
                        "41st Avenue",  # R4
                        "Hastings St",  # R5
                        "Scott Road",  # R6
                        "SeaBus")

routes = {}

with open("GTFS data/routes.txt", "r") as routes_file:
    routes_read = csv.DictReader(routes_file)

    for row in routes_read:
        if row["route_long_name"] in tracked_routes_names:
            routes[row["route_id"]] = [row["route_long_name"],
                                       row["route_short_name"],
                                       row["route_color"]]

trips = {route_id: [] for route_id in routes}

with open("GTFS data/trips.txt", "r") as trips_file:
    trips_read = csv.DictReader(trips_file)

    for row in trips_read:
        route_id = row["route_id"]
        if route_id in trips:
            trips[route_id].append(row["trip_id"])

stops = {trip_id: [] for route_trip in trips.values()
         for trip_id in route_trip}

with open("GTFS data/stop_times.txt", "r") as stop_times_file:

    # using csv.reader for faster loading times
    stop_times_read = csv.reader(stop_times_file)
    stop_times_header = next(stop_times_read)

    stop_id_index = stop_times_header.index("stop_id")
    trip_id_index = stop_times_header.index("trip_id")
    arrival_time_index = stop_times_header.index("arrival_time")
    departure_time_index = stop_times_header.index("departure_time")
    stop_sequence_index = stop_times_header.index("stop_sequence")

    for row in stop_times_read:
        trip_id = row[trip_id_index]
        trip_list_reference = stops.get(trip_id)

        if trip_list_reference is not None:
            trip_list_reference.append(stop_class.stop(row[stop_id_index],
                                                       row[trip_id_index],
                                                       row[arrival_time_index],
                                                       row[departure_time_index],
                                                       row[stop_sequence_index]))

for trip in stops:
    stops[trip].sort(key=lambda stop: int(stop.stop_sequence))

for route in routes:
    for trip in trips[route]:
        heapq.heappush(q, vehicle_class.vehicle(
            route, trip, stops[trip], None))

print(q[0])

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
