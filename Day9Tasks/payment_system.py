class Payment:
    def process_payment(self, amount):
        print(f"Processing payment of {amount} using a generic method.")


class CreditCard(Payment):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} using Credit Card.")


class UPI(Payment):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} using UPI.")


class NetBanking(Payment):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} using Net Banking.")


payment1 = CreditCard()
payment2 = UPI()
payment3 = NetBanking()

payments = [payment1, payment2, payment3]

for payment in payments:
    payment.process_payment(1500)
    