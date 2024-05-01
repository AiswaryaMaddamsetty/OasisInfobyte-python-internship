def calculate_BMI(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_BMI(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator")
    print("----------------------------")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_BMI(weight, height)
    weight_classification = classify_BMI(bmi)

    print("\nBMI Result:")
    print(f"Your BMI is: {bmi:.2f}")

    if weight_classification == "Underweight":
        print("You are classified as underweight. It's important to maintain a healthy weight.")
    elif weight_classification == "Normal weight":
        print("Congratulations! You are within the normal weight range. Keep up the good work!")
    elif weight_classification == "Overweight":
        print("You are classified as overweight. Consider making lifestyle changes to improve your health.")
    else:
        print("You are classified as obese. It's important to prioritize your health and consider making lifestyle changes.")
if __name__ == "__main__":
    main()

