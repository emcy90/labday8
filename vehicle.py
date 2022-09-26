"""
vehicle
"""


class Vehicle:
    """python class location that stores data."""

    def __init__(self, vehicle_no, bike, truck, capacity, current_status):
        self.vehicle_no = vehicle_no
        self.truck = truck
        self.bike = bike
        self.capacity = capacity
        self. current_status = current_status "[Free,busy,Not_working]"

    def __str__(self):
        return self.short_string()

    def short_string(self) -> str:
        """function to return vehicle as string"""
        return f"bike and truck {self.bike}, {self.truck}"
