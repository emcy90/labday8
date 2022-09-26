from user import User
from order import Order
"""
main for logistics system
"""


def register_new_user(User):
    """method to register a new user"""
    person1 = User(9, 'Anders Karsson', 'gamlestadsgatan 42', '0703689567', 'anders_5@gmail.com')
    person2 = User(1, 'Ford Prefect', 'mjaugatan 42', '0769856985', 'art@gmail.com')


def take_an_order(Order):
    """Deliver it to a given destination"""

    #order1 = Order(7, 'low', 'Coop', None and None,

    # User
    # order id
    # location
    # vehicle status
    # payment status



def take_orders():
    """method to handle the order that was taken"""
    pass


def process_an_order():
    """method to process an order"""
    pass


def track_order():
    """method to track the order"""
    pass


def cancel_order():
    """method to cancel order"""
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    take_orders()
    take_an_order()
    process_an_order()
    track_order()
    cancel_order()
    register_new_user()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
