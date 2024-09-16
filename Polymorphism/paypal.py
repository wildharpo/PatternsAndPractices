from payment_base import *

class PayPal(PaymentBase):
    def process_payment(self):
        msg = f"PayPal payment: {self.amount}"
        print(msg)