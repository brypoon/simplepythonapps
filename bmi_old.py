# bmi calculator

# for metric, BMI = (weight in kg / height in metres squared)
# for imperial, BMI = (weight in pounds / height in inches squared) * 703

def gather_info():
    system = input("Are your measurements in [m]etric or [i]mperial units? ").lower().strip()
    if system.startswith("i"):
        height = float(input("What is your height (inches)? "))
        weight = float(input("What is your weight (pounds)? "))
    elif system.startswith("m"):
        height = float(input("What is your height (metres)? "))
        weight = float(input("What is your weight (kilograms)? "))

    return weight, height, system

def calculate_bmi(weight, height, system="metric"):
    """
    Return the Body Mass Index (BMI) for the given weight, height and measurement system.
    """
    if system == "metric":
        bmi = (weight/(height ** 2))
    else:
        bmi = 703 * (weight/(height ** 2))
    return bmi

while True:
    weight, height, system = gather_info()
    if system.startswith("i"):
        bmi = calculate_bmi(weight, height, system)
        print(f"Your BMI is {bmi}.")
        break
    elif system.startswith("m"):
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi}.")
        break
    else:
        system = input("Error: Unknown measurement system. Please use imperial or metric: ").lower().strip()
        if system.startswith("i"):
            bmi = calculate_bmi(weight, height, system)
            print(f"Your BMI is {bmi}.")
            break
        elif system.startswith("m"):
            bmi = calculate_bmi(weight, height, system)
            print(f"Your BMI is {bmi}.")
            break
