"""
order
"""
from typing import Optional
from dataclasses import dataclass


class Order:
    """python class order that stores data about Order."""

    def __init__(self, orderid, order_priority, sender, location, payment_details, items_list, total_weight, order_status,
                 order_place_time, order_delivery_time, vehicle):
        self.orderid = orderid
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

    def get_order_priority(self) -> str:
        """Returns which current status"""
        return self.current_order_priority

    def get_order_status(self) -> str:
        """returns which current order status"""
        return self.current_order_status


@dataclass
class Status:
    current_order_priority: Optional[Order] = None
    current_order_status: Optional[Order] = None

    def priority_status(self) -> str:
        """priority status"""
        witch_status = self.current_order_priority.get_order_priority()
        if self.current_order_priority is not None:
            return witch_status

    def order_status(self) -> str:
        """order status"""
        witch_status = self.current_order_status.get_order_status()
        if self.current_order_status is not None:
            return witch_status
