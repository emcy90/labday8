from typing import Optional
from dataclasses import dataclass
"""
payment-details
"""


class PaymentDetail:
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
        return f"payment method and payment status {self.payment_method}, {self.payment_status}"

    def pay_method(self) -> str:
        """Returns which payment method"""
        return self.payment_method

    def pay_status(self) -> str:
        """Returns which payment status"""
        return self.payment_status


@dataclass
class Payment:
    payment_status: Optional[PaymentDetail] = None
    payment_method: Optional[PaymentDetail] = None

    def payment_stat(self) -> str:
        """payment status."""
        witch_payment_status = self.payment_status.pay_status()
        if self.payment_status is not None:
            return witch_payment_status

    def payment_met(self) -> str:
        """payment method."""
        witch_payment_method = self.payment_method.pay_method()
        if self.payment_method is not None:
            return witch_payment_method
