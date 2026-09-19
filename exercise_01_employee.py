# Base Class (Parent)
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name       : {self.name}")


# Derived Class (Child demonstrating Single Inheritance)
class Manager(Employee):
    def __init__(self, name, employee_id, department):
        # super().__init__() passes name and employee_id up to Employee
        super().__init__(name, employee_id)
        self.department = department

    def display_details(self):
        # Call the parent method, then display the manager-specific attribute
        super().display_details()
        print(f"Department : {self.department}")


# Driver Code
if __name__ == "__main__":
    print("=== Manager Record ===")
    mgr = Manager("Alice Smith", "EMP-1042", "Cybersecurity Operations")
    mgr.display_details()
