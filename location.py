"""
location
"""

class Location:
    """python class location that stores data."""

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return self.short_string()

    def short_string(self) -> str:
        """function to return longitude and latitude as string"""
        return f"Longitude and latitude {self.longitude}, {self.latitude}"

    def create_location(self):
        """create location"""
        location1 = Location(0, 0)