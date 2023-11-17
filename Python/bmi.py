def get_user_input():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        return weight, height
    except ValueError as e:
        print(f"Error: {e}")
        return get_user_input()

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    while True:
        weight, height = get_user_input()
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

        # Ask the user if they want to calculate BMI again
        another_calculation = input("Do you want to calculate BMI again? (yes/no): ").lower()
        if another_calculation != 'yes':
            break

if __name__ == "__main__":
    main()
