import time

def user_input(Input):
    while True:
        try:
            value = str(input(f"Enter your {Input}: ")).replace(",",".")
            valuex = float(value)
            break
        except ValueError:
            print("Please enter a valid number")
    return valuex

def BMICalculator():

    Height = user_input("Height")
    Weight = user_input("Weight")

    Result = Weight / (Height / 100) ** 2
    print("Your BMI is: ", round(Result, 1))

    if Result <= 18.5:
        print("You are underweight")
    elif Result <= 24.9:
        print("You are healthy")
    elif Result <= 29.9:
        print("You are overweight")
    elif Result > 29.9:
        print("You are obese")


def enter_again():
    user = input("Do you want to enter again?: ").lower()

    while user not in ['yes', 'y', 'no', 'n']:
        print("Please enter a valid input")
        user = input("Do you want to enter again?: ").lower()
    if user not in ['yes', 'y']:
        print("Have a nice day!")
        time.sleep(1)
    while user not in ['no','n']:
        BMICalculator()
        enter_again()


print("BMICalculator by Faisal!")
BMICalculator()
enter_again()