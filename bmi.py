# bmi calculator
# for metric, BMI = (weight in kg / height in metres squared)
# for imperial, BMI = (weight in pounds / height in inches squared) * 703

# import collections
#
# Measurements = collections.namedtuple('Measurements', 'weight height system')


def gather_info():
    system = input("Are your measurements in [m]etric or [i]mperial units? ")

    while not (system.startswith("i")) and not (system.startswith("m")):
        system = input(
            "Error: Unknown measurement system. Please use [m]etric or [i]mperial: ")

    if system.startswith("i"):
        h = "inches"
        w = "pounds"
    elif system.startswith("m"):
        h = "metres"
        w = "kilograms"

    height = float(input(f"What is your height (in {h})? "))
    weight = float(input(f"What is your weight (in {w})? "))

    return weight, height, system


def calculate_bmi(weight, height, system):
    """
    Return the Body Mass Index (BMI) for the given weight, height and measurement system.
    """
    if system.startswith("i"):
        bmi = 703 * (weight / (height ** 2))
    elif system.startswith("m"):
        bmi = (weight / (height ** 2))

    return bmi


def report_bmi(bmi):
    if bmi <= 18.4:
        condition = "You are underweight and at risk for nutritional deficiency diseases and osteoporosis."
    elif 18.5 <= bmi <= 22.9:
        condition = "You are in the healthy range."
    elif 23 <= bmi <= 27.4:
        condition = "You are fat and your health is at moderate risk."
    elif 27.5 <= bmi:
        condition = "You are VERY fat and your health is at high risk."

    print(f"Your BMI is {bmi}. {condition}")


def main():
    weight, height, system = gather_info()
    bmi = calculate_bmi(weight, height, system)
    report_bmi(bmi)


if __name__ == "__main__":
    main()
