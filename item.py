class Item:
    """Class user that stores data."""

    def __init__(self, item_name, price, volume, weight):
        self.item_name = item_name
        self.price = price
        self.volume = volume
        self.weight = weight

    def __str__(self):
        return self.short_string()

    def short_string(self) -> str:
        """function to return items as string"""
        return f" item name {self.item_name}"
