class UniversityConfig:
    # 1. Protected class variable to hold the single shared instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        # 2. Intercept object creation: only allocate memory if no instance exists
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialize configuration attributes
            cls._instance._university_name = ""
            cls._instance._academic_year = ""
            cls._instance._semester = ""
        return cls._instance

    # Method to set the configuration
    def set_config(self, university_name: str, academic_year: str, semester: str):
        self._university_name = university_name
        self._academic_year = academic_year
        self._semester = semester
        print(f"[Config Updated] Configuration saved by instance {id(self)}")

    # Method to display the current configuration
    def display_config(self):
        print("\n--- Current University Configuration ---")
        print(f"University Name: {self._university_name}")
        print(f"Academic Year  : {self._academic_year}")
        print(f"Semester       : {self._semester}")
        print(f"Instance ID    : {id(self)}")
        print("----------------------------------------\n")


# ==========================================
# Verification & Execution (Tasks 4 to 7)
# ==========================================
if __name__ == "__main__":
    # Task 4: Create three separate variables from UniversityConfig
    config1 = UniversityConfig()
    config2 = UniversityConfig()
    config3 = UniversityConfig()

    # Task 5: Set configuration using the first object (config1)
    print("Setting configuration using config1:")
    config1.set_config(
        university_name="Auckland Institute of Technology",
        academic_year="2026-2027",
        semester="Semester 2"
    )

    # Task 6: Display configuration using another object (config2)
    print("Reading configuration using config2:")
    config2.display_config()

    # Task 7: Use 'is' operator to verify all variables refer to the exact same instance
    print("=== Identity Verification Using 'is' Operator ===")
    print(f"config1 is config2 : {config1 is config2}")
    print(f"config2 is config3 : {config2 is config3}")
    print(f"config1 is config3 : {config1 is config3}")

    print(f"\nMemory address of config1: {hex(id(config1))}")
    print(f"Memory address of config2: {hex(id(config2))}")
    print(f"Memory address of config3: {hex(id(config3))}")