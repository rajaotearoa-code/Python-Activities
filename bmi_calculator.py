# ==============================================================================
# CLI Body Mass Index (BMI) Calculator
# Description: Calculates BMI based on weight (kg) and height (m) input
#              and classifies the result into standard WHO categories.
# ==============================================================================

def calculate_bmi(weight_kg, height_m):
    """
    Calculates the BMI value given weight in kilograms and height in meters.
    Formula: weight / (height ^ 2)
    """
    return weight_kg / (height_m ** 2)


def get_bmi_category(bmi):
    """
    Determines the health category based on standard WHO BMI thresholds.
    """
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
    Main function to execute the CLI BMI Calculator application.
    Handles user interaction, input validation, and output formatting.
    """
    print("=" * 45)
    print("      BODY MASS INDEX (BMI) CALCULATOR      ")
    print("=" * 45)

    try:
        # Prompt user for inputs and convert to float data type
        weight = float(input("Enter your weight in kilograms (e.g., 70): "))
        height = float(input("Enter your height in meters (e.g., 1.75): "))

        # Input validation: Height and weight must be positive numbers
        if weight <= 0 or height <= 0:
            print("\n[Error]: Weight and height must be positive numbers greater than zero.")
            return

        # Perform calculation and category lookup
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        # Output results formatted to 2 decimal places
        print("\n" + "-" * 45)
        print("RESULTS:")
        print(f"  * Calculated BMI : {bmi:.2f}")
        print(f"  * Category       : {category}")
        print("-" * 45)

    except ValueError:
        # Error handling for non-numeric inputs (e.g., letters)
        print("\n[Error]: Invalid input. Please enter numerical values only.")


# Entry point of the program
if __name__ == "__main__":
    main()