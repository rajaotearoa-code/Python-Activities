# ==============================================================================
# OOP Body Mass Index (BMI) Calculator
# Description: Refactored using OOP style (Class & Methods without __init__)
# ==============================================================================

class BMICalculator:
    """
    Class containing methods to perform BMI calculations and category lookups.
    """
    def calculate_bmi(self, weight_kg, height_m):
        """Calculates BMI value given weight (kg) and height (m)."""
        return weight_kg / (height_m ** 2)

    def get_category(self, bmi):
        """Determines health category based on WHO BMI thresholds."""
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25.0:
            return "Normal weight"
        elif 25.0 <= bmi < 30.0:
            return "Overweight"
        else:
            return "Obesity"


def main():
    """
    Main function to run the CLI interface and interact with the BMICalculator class.
    """
    print("=" * 45)
    print("    BODY MASS INDEX (BMI) CALCULATOR (OOP)    ")
    print("=" * 45)

    # 1. Instantiate the object (no __init__ arguments needed)
    calculator = BMICalculator()

    try:
        weight = float(input("Enter your weight in kilograms (e.g., 70): "))
        height = float(input("Enter your height in meters (e.g., 1.75): "))

        if weight <= 0 or height <= 0:
            print("\n[Error]: Weight and height must be positive numbers.")
            return

        # 2. Call methods on the 'calculator' object using dot notation
        bmi = calculator.calculate_bmi(weight, height)
        category = calculator.get_category(bmi)

        print("\n" + "-" * 45)
        print("RESULTS:")
        print(f"  * Calculated BMI : {bmi:.2f}")
        print(f"  * Category       : {category}")
        print("-" * 45)

    except ValueError:
        print("\n[Error]: Invalid input. Please enter numerical values only.")


if __name__ == "__main__":
    main()