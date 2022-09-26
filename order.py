"""
order
"""
from typing import Optional
from dataclasses import dataclass


class Order:
    """python class order that stores data about Order."""

    def __init__(self, orderid, order_priority, sender, location, payment_details, items_list, total_weight,
                 order_status, order_place_time, order_delivery_time, vehicle):
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

    def order_prio(self) -> str:
        """Returns which current status"""
        return self.order_priority

    def order_stat(self) -> str:
        """returns which current order status"""
        return self.order_status

    def create_order(self):
        """create_order"""
        #order1 = Order(7, 'low', 'Coop', None, 'Visa 4568',


@dataclass
class OrderDetails:
    """details about priority_status and order status"""
    order_priority: Optional[Order] = None
    order_status: Optional[Order] = None

    def priority_stat(self) -> str:
        """priority status"""
        witch_priority_status = self.order_priority.order_prio()
        if self.order_priority is not None:
            return witch_priority_status

    def order_stat(self) -> str:
        """order status"""
        witch_status = self.order_status.order_stat()
        if self.order_status is not None:
            return witch_status



