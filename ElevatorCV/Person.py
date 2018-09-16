class Person:

    def __init__(self, arrival_floor, destination_floor):
        self._start = arrival_floor
        self._end = destination_floor
        self._timer = 0

    def move_floors(self, floors):
        self._timer = self._timer + (floors * 5)

    def stop_at_floor(self):
        self._timer = self._timer + 10

    def set_start(self, floor):
        self._start = floor

    def set_end(self, floor):
        self._end = floor

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def get_wait_time(self):
        return self._timer

    def add_wait_time(self, time):
        self._timer += time
