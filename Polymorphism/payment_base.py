class PaymentBase:
    def __init__(self, amount: int):
        self.amount:int = amount

    def process_payment(self):
        pass