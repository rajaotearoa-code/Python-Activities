# ==============================================================================
# OOP Student Information Collector & Age Classifier
# Description: Collects personal info for multiple students, sorts them by age,
#              and displays the results. Contains detailed data type explanations.
# ==============================================================================

class Student:
    """
    Represents an individual student's personal profile.
    """

    def __init__(self, full_name, age, address, student_id):
        # Data Type: str (string) -> Stores text sequence for the student's name
        self.full_name = str(full_name)

        # Data Type: int (integer) -> Stores whole numbers representing age
        self.age = int(age)

        # Data Type: str (string) -> Stores text representation of physical address
        self.address = str(address)

        # Data Type: str (string) -> Stores alphanumeric text for unique identification
        self.student_id = str(student_id)

    def display_details(self):
        """Displays formatted attributes of the student instance."""
        print(f"ID: {self.student_id:<10} | Name: {self.full_name:<20} | Age: {self.age:<3} | Address: {self.address}")


class StudentRegistry:
    """
    Manages collection, sorting, and display of multiple Student objects.
    """

    def __init__(self):
        # Data Type: list -> An ordered, mutable collection containing Student objects
        self.students = []

    def add_student(self, student):
        """Adds a Student object instance to the registry list."""
        # Data Type: Student (custom class object) -> Appended into self.students list
        self.students.append(student)

    def collect_student_data(self):
        """
        Interactively prompts user to enter details for an unknown number of students
        until the user chooses to stop by typing 'done'.
        """
        print("=" * 60)
        print("         STUDENT INFORMATION COLLECTION SYSTEM          ")
        print("=" * 60)
        print("Note: Enter student details below. Type 'done' as the name to finish.\n")

        # Data Type: int (integer) -> Counter keeping track of entered record count
        record_number = 1

        while True:
            # Data Type: str (string) -> User input for full name
            full_name = input(f"[{record_number}] Enter Full Name (or 'done' to stop): ").strip()

            # Terminal condition check
            if full_name.lower() == "done":
                break

            # Input validation loop for numerical Age input
            while True:
                try:
                    # Data Type: int (integer) -> Converted from user input string
                    age = int(input("    Enter Age: ").strip())
                    if age <= 0:
                        print("    [!] Age must be a positive number greater than 0.")
                        continue
                    break
                except ValueError:
                    # Exception handling for non-numeric input errors
                    print("    [!] Invalid input! Please enter a numerical whole number for age.")

            # Data Type: str (string) -> User input for address
            address = input("    Enter Address: ").strip()

            # Data Type: str (string) -> User input for student ID
            student_id = input("    Enter Student ID: ").strip()

            # Data Type: Student -> Instantiating a new Student object instance
            new_student = Student(
                full_name=full_name,
                age=age,
                address=address,
                student_id=student_id
            )

            # Store student object in the registry list
            self.add_student(new_student)
            
            record_number += 1
            print("-" * 60)

    def sort_students_by_age(self):
        """
        Sorts the internal students list in ascending order by age.
        """
        # Data Type: bool (boolean) -> Re-ordering list items in-place using key lambda function
        # The key lambda extracts the integer 'age' property from each Student object
        self.students.sort(key=lambda student: student.age)

    def display_all_students(self):
        """
        Displays all collected student records after sorting.
        """
        if not self.students:
            print("\n[!] No student records were entered.")
            return

        print("\n" + "=" * 70)
        print("       SORTED STUDENT RECORDS (BY AGE - ASCENDING)       ")
        print("=" * 70)

        # Data Type: Student -> Iterating over each object in the list
        for student in self.students:
            student.display_details()

        print("=" * 70)
        print(f"Total Students Processed: {len(self.students)}")


def main():
    """Main program execution flow."""
    # Data Type: StudentRegistry (custom class object instance)
    registry = StudentRegistry()

    # Step 1: Collect data
    registry.collect_student_data()

    # Step 2: Sort records by age
    registry.sort_students_by_age()

    # Step 3: Display output
    registry.display_all_students()


if __name__ == "__main__":
    main()