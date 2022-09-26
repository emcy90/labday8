"""
payment-details
"""

class Payment_detail:
    """python class payment-details that stores data about payments."""

    def __init__(self, payment_method, transition_id, amount, payment_status, cardnumber):
        self.payment_method = payment_method
        self.transition_id = transition_id
        self.amount = amount
        self.payment_status = payment_status
        self.cardnumber = cardnumber

    def __str__(self):
        return self.short_string()

    def short_string(self) -> str:
        """function to return payment_method and payment_status as string"""
        return f"Longitude and latitude {self.payment_method}, {self.payment_status}"
