class Person:
    """Base class representing any individual in the university."""
    def __init__(self, person_id: str, name: str):
        self.id = person_id
        self.name = name

    def display_details(self):
        print(f"ID: {self.id} | Name: {self.name}")


class Student(Person):
    """Derived class representing a student."""
    def __init__(self, person_id: str, name: str, student_id: str):
        super().__init__(person_id, name)
        self.student_id = student_id

    def display_details(self):
        super().display_details()
        print(f"Student ID: {self.student_id}")


class Staff(Person):
    """Derived class representing university employees."""
    def __init__(self, person_id: str, name: str, staff_id: str, tax_num: str):
        super().__init__(person_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display_details(self):
        super().display_details()
        print(f"Staff ID: {self.staff_id} | Tax Number: {self.tax_num}")


class Academic(Staff):
    """Derived from Staff: Represents lecturers and researchers."""
    def __init__(self, person_id: str, name: str, staff_id: str, tax_num: str):
        super().__init__(person_id, name, staff_id, tax_num)
        self.publications = []

    def add_publication(self, publication_title: str):
        """Records a research publication."""
        self.publications.append(publication_title)

    def calculate_publications(self) -> int:
        """Calculates and returns the total count of publications."""
        return len(self.publications)

    def display_publication_record(self):
        """Displays lecturer details and total publications."""
        print("\n==========================================")
        print("         ACADEMIC / LECTURER RECORD       ")
        print("==========================================")
        self.display_details()
        total = self.calculate_publications()
        print(f"Total Publications: {total}")
        if self.publications:
            print("Publications List:")
            for index, title in enumerate(self.publications, start=1):
                print(f"  {index}. {title}")


class General(Staff):
    """Derived from Staff: Represents general/administrative staff."""
    def __init__(self, person_id: str, name: str, staff_id: str, tax_num: str, rate_of_pay: float):
        super().__init__(person_id, name, staff_id, tax_num)
        self.rate_of_pay = rate_of_pay
        self.hours_worked = 0.0

    def record_hours(self, hours: float):
        """Logs worked hours for payroll calculation."""
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        self.hours_worked += hours

    def calculate_total_pay(self) -> float:
        """Calculates gross pay based on hours worked and rate of pay."""
        return self.rate_of_pay * self.hours_worked

    def display_pay_info(self):
        """Displays general staff pay rate and calculated earnings."""
        total_pay = self.calculate_total_pay()
        print("\n==========================================")
        print("        GENERAL STAFF PAYROLL RECORD      ")
        print("==========================================")
        self.display_details()
        print(f"Standard Pay Rate: ${self.rate_of_pay:.2f} / hr")
        print(f"Hours Worked:      {self.hours_worked:.2f} hrs")
        print(f"Total Gross Pay:   ${total_pay:.2f}")


# ==========================================
# Demonstration & Output Verification
# ==========================================
if __name__ == "__main__":
    # 1. Academic (Lecturer) Instance
    lecturer = Academic(
        person_id="P-9001",
        name="Dr. Aris Thorne",
        staff_id="STF-401",
        tax_num="TX-8839201"
    )
    lecturer.add_publication("Distributed Consensus in Fault-Tolerant Networks (2024)")
    lecturer.add_publication("Analysis of Zero-Trust Security Protocols (2025)")
    lecturer.add_publication("Edge Computing Architectures in Modern IoT (2026)")

    # Calculate and display publication metrics
    lecturer.display_publication_record()

    # 2. General Staff Instance
    admin_staff = General(
        person_id="P-9002",
        name="Elena Rostova",
        staff_id="STF-809",
        tax_num="TX-5510492",
        rate_of_pay=36.50
    )
    admin_staff.record_hours(40.0)

    # Calculate and display pay rate and total pay
    admin_staff.display_pay_info()