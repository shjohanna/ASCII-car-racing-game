import random


class Track:
    def __init__(self, length):
        self.length = length
        self.lane_one = []
        self.lane_two = []
        self.range = range(0, length)
        for _ in self.range:
            self.lane_one.append("_")
            self.lane_two.append("_")
        self.lane_one.append("|")
        self.lane_two.append("|")


track = Track(random.randint(8, 11))
