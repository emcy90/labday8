"""
order
"""

class Order:
    """python class order that stores data about Order."""

    def __init__(self, id, order_priority, sender, location, payment_details, items_list, total_weight, order_status,
                 order_place_time, order_delivery_time, vehicle):
        self.id = id
        self.order_priority = order_priority
        self.sender = sender
        self.location = location
        self.payment_details = payment_details
        self.items_list = items_list
        self.total_weight = total_weight
        self.order_status = order_status
        self.order_place_time = order_place_time
        self.order_delivery_time = order_delivery_time
        self.vehicle = vehicle

    def __str__(self):
        return self.short_string()

    def short_string(self) -> str:
        """function to return order-priority and order-status as string"""
        return f" order-priority and order-status{self.order_priority}, {self.order_status}"