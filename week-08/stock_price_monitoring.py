from abc import ABC, abstractmethod


# ==========================================
# Task 1: Create the Observer Interface
# ==========================================
class Observer(ABC):
    @abstractmethod
    def update(self, price):
        pass


# ==========================================
# Task 2: Create the Concrete Observer
# ==========================================
class Investor(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(f"{self.name} received new stock price: {price}")


# ==========================================
# Task 3: Create the Subject
# ==========================================
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.investors = []

    def subscribe(self, investor):
        self.investors.append(investor)

    def unsubscribe(self, investor):
        self.investors.remove(investor)

    def notify(self):
        for investor in self.investors:
            investor.update(self.price)

    # Task 4: Method to change price and alert observers
    def set_price(self, new_price):
        self.price = new_price
        self.notify()


# ==========================================
# Execution & Verification
# ==========================================
if __name__ == "__main__":
    # Create the stock
    apple_stock = Stock("AAPL", 100)

    # Create investors
    ali = Investor("Ali")
    bob = Investor("Bob")

    # Subscribe investors
    apple_stock.subscribe(ali)
    apple_stock.subscribe(bob)

    # Task 4: Change stock price to 105
    apple_stock.set_price(105)