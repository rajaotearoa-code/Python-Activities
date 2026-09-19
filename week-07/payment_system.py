# 1. Credit Card Class
class CreditCard:
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def make_payment(self, amount):
        print(f"[Credit Card] Charged ${amount:.2f} to card ending in {self.card_number[-4:]} ({self.card_holder}).")


# 2. PayPal Class
class PayPal:
    def __init__(self, email):
        self.email = email

    def make_payment(self, amount):
        print(f"[PayPal] Sent ${amount:.2f} using account {self.email}.")


# 3. Bank Transfer Class
class BankTransfer:
    def __init__(self, account_number, bank_code):
        self.account_number = account_number
        self.bank_code = bank_code

    def make_payment(self, amount):
        print(f"[Bank Transfer] Wired ${amount:.2f} from account {self.account_number} (Bank: {self.bank_code}).")


# --- Demonstration of Polymorphism ---
if __name__ == "__main__":
    # Create distinct objects from each class
    visa = CreditCard("4111222233334444", "John Doe")
    pp = PayPal("john.doe@example.com")
    wire = BankTransfer("NZ12-3456-7890123-00", "ANZ")

    # Put different objects into one list
    payment_methods = [visa, pp, wire]

    print("=== Processing polymorphic payments ===")
    
    # One uniform call triggers three completely different operations
    for method in payment_methods:
        method.make_payment(250.00)