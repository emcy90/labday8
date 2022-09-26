from typing import Optional
from dataclasses import dataclass
"""
vehicle
"""


class Vehicle:
    """python class vehicle stores data."""

    def __init__(self, vehicle_no, bike, truck, capacity, current_status):
        self.vehicle_no = vehicle_no
        self.truck = truck
        self.bike = bike
        self.capacity = capacity
        self. current_status = current_status

    def __str__(self):
        return self.short_string()

    def short_string(self) -> str:
        """function to return vehicle as string"""
        return f"bike and truck {self.bike}, {self.truck}"

    def get_status(self) -> str:
        """Returns which current status"""
        return self.current_status


@dataclass
class Status:
    current_status: Optional[Vehicle] = None

    def status(self) -> str:
        """which person is specific course."""
        witch_status = self.current_status.get_status()
        if self.current_status is not None:
            return witch_status


