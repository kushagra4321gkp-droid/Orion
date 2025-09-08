weight = float(input("Enter your weight : "))

height = float(input("Enter your height : "))

bmi = round((weight/height**2), 0)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight. ")
elif bmi < 25:
    print(f"Your BMI is {bmi}, your weight is Normal. ")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight. ")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese. ")
else:
    print(f"Your BMI is {bmi}, you are clinically obese. ")

print("Eat Healthy")
