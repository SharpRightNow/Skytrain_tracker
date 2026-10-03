class stop:
    __slots__ = ("stop_id", "trip_id", "arrival_time", "departure_time", "stop_sequence")

    def __init__(self, stop_id, trip_id, arrival_time, departure_time, stop_sequence):
        self.stop_id = stop_id
        self.trip_id = trip_id
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.stop_sequence = stop_sequence
    def __repr__(self):
            return f"e "