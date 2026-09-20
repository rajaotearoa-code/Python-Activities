from abc import ABC, abstractmethod


# ==========================================
# PART 1: The Product (TravelPackage)
# ==========================================
class TravelPackage:
    def __init__(self):
        self.destination = None
        self.hotel = None
        self.transport = None
        self.meal_plan = None
        self.activities = []
        self.insurance = False

    def display(self):
        print("\n==================================")
        print("      TRAVEL PACKAGE SUMMARY      ")
        print("==================================")
        print(f"Destination : {self.destination}")
        print(f"Hotel       : {self.hotel}")
        print(f"Transport   : {self.transport}")
        print(f"Meal Plan   : {self.meal_plan}")
        print(f"Activities  : {', '.join(self.activities) if self.activities else 'None'}")
        print(f"Insurance   : {'Yes' if self.insurance else 'No'}")
        print("==================================\n")


# ==========================================
# PART 2: The Builder Interface (Abstract)
# ==========================================
class TravelPackageBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_destination(self, destination: str):
        pass

    @abstractmethod
    def set_hotel(self, hotel: str):
        pass

    @abstractmethod
    def set_transport(self, transport: str):
        pass

    @abstractmethod
    def set_meal_plan(self, meal_plan: str):
        pass

    @abstractmethod
    def add_activity(self, activity: str):
        pass

    @abstractmethod
    def set_insurance(self, insurance: bool):
        pass

    @abstractmethod
    def get_package(self) -> TravelPackage:
        pass


# ==========================================
# PART 3: The Concrete Builder
# ==========================================
class ConcreteTravelPackageBuilder(TravelPackageBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._package = TravelPackage()

    def set_destination(self, destination: str):
        self._package.destination = destination
        return self

    def set_hotel(self, hotel: str):
        self._package.hotel = hotel
        return self

    def set_transport(self, transport: str):
        self._package.transport = transport
        return self

    def set_meal_plan(self, meal_plan: str):
        self._package.meal_plan = meal_plan
        return self

    def add_activity(self, activity: str):
        self._package.activities.append(activity)
        return self

    def set_insurance(self, insurance: bool):
        self._package.insurance = insurance
        return self

    def get_package(self) -> TravelPackage:
        constructed_package = self._package
        self.reset()
        return constructed_package


# ==========================================
# PART 4: Execution / Client Code
# ==========================================
if __name__ == "__main__":
    builder = ConcreteTravelPackageBuilder()

    # Constructing a fully customized vacation step-by-step
    custom_trip = (
        builder.set_destination("Auckland")
        .set_hotel("5-star")
        .set_transport("Flight")
        .set_meal_plan("Full Board")
        .add_activity("City Tour")
        .add_activity("Adventure Tour")
        .set_insurance(True)
        .get_package()
    )

    custom_trip.display()

    # Constructing a budget getaway without insurance or extra activities
    weekend_trip = (
        builder.set_destination("Sydney")
        .set_hotel("3-star")
        .set_transport("Bus")
        .set_meal_plan("Breakfast")
        .get_package()
    )

    weekend_trip.display()

