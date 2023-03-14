weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in m : "))

bmi = weight / height**2
bmi = round(bmi, 2)

if (bmi < 18.5):
    print(f"Your bmi is {bmi} and you are underweight")
elif (bmi < 25):
    print(f"Your bmi is {bmi} and you have normal weight")
elif (bmi < 30):
    print(f"Your bmi is {bmi} and you are overweight")
elif (bmi < 35):
    print("Your bmi is {bmi} and your are obese")
else:
    print(f"Your bmi is {bmi} and you are clinically obese")

                   