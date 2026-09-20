from abc import ABC, abstractmethod


# ==========================================
# PART 1: The Component Interface
# ==========================================
class Car(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


# ==========================================
# PART 2: The Concrete Component
# ==========================================
class BasicCar(Car):
    def get_cost(self) -> float:
        return 25000.00

    def get_description(self) -> str:
        return "Basic Car"


# ==========================================
# PART 3: The Base Decorator
# ==========================================
class CarDecorator(Car):
    def __init__(self, car: Car):
        self._car = car

    def get_cost(self) -> float:
        return self._car.get_cost()

    def get_description(self) -> str:
        return self._car.get_description()


# ==========================================
# PART 4: Concrete Decorators
# ==========================================
class GPS(CarDecorator):
    def get_cost(self) -> float:
        return self._car.get_cost() + 500.00

    def get_description(self) -> str:
        return f"{self._car.get_description()} + GPS"


class Sunroof(CarDecorator):
    def get_cost(self) -> float:
        return self._car.get_cost() + 1000.00

    def get_description(self) -> str:
        return f"{self._car.get_description()} + Sunroof"


class LeatherSeats(CarDecorator):
    def get_cost(self) -> float:
        return self._car.get_cost() + 1500.00

    def get_description(self) -> str:
        return f"{self._car.get_description()} + Leather Seats"


class PremiumSound(CarDecorator):
    def get_cost(self) -> float:
        return self._car.get_cost() + 800.00

    def get_description(self) -> str:
        return f"{self._car.get_description()} + Premium Sound System"


# ==========================================
# PART 5: Execution / Client Code
# ==========================================
if __name__ == "__main__":
    print("=== Custom Car Configuration ===\n")

    # Order 1: Base car only
    car1 = BasicCar()
    print(f"Description: {car1.get_description()}")
    print(f"Total Price: ${car1.get_cost():,.2f}\n")

    # Order 2: Basic Car + Sunroof + GPS
    # Dynamically wrapping objects inside objects
    car2 = BasicCar()
    car2 = Sunroof(car2)
    car2 = GPS(car2)
    print(f"Description: {car2.get_description()}")
    print(f"Total Price: ${car2.get_cost():,.2f}\n")

    # Order 3: Fully loaded car (all options wrapped in a single expression)
    car3 = PremiumSound(LeatherSeats(Sunroof(GPS(BasicCar()))))
    print(f"Description: {car3.get_description()}")
    print(f"Total Price: ${car3.get_cost():,.2f}")