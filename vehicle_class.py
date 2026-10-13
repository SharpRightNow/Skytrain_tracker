import datetime

class vehicle:
    def __init__(self, route, trip_id, stops, start_time):
        self.route = route
        self.trip_id = trip_id
        self.stops = stops

        # TODO: Fix this
        self.next_light_time = (
            datetime.datetime.now() + datetime.timedelta(seconds=5))

        # TODO: Make current light figure out what it should be at the start_time
        # will include both current stop and current light within that stop
        self.current_light = None
        self.a = 0

    def __lt__(self, other):
        # Compare vehicles based on their next light time
        return self.next_light_time < other.next_light_time

    # Make the class print out nicely when printed

    def __repr__(self):
        return f"Vehicle(route={self.route}, trip_id={self.trip_id}, next_light_time={self.next_light_time}, next_light={self.get_next_light()}, current_light={self.get_current_light()})"

    def move_to_next_light(self):
        self.a += 1

        # Move where the vehicle thinks it is to match where it is (move it to the next light)
        pass

    def get_next_light(self):
        # current pos/light will be stored as a tuple of ("stop_id", light_number)
        # Return the next light that the vehicle will be at
        pass

    def get_current_light(self):
        # Return the current light that the vehicle is at
        pass

    def get_next_light_time(self):
        # TODO: Make this return the time of the next light
        return (datetime.datetime.now() + datetime.timedelta(seconds=5))


# TODO: make sure next_light_time is updated
