weight=float(input("Enter your weight in kilograms"))
height=float(input("Enter your height in metres"))
bmi=weight / (height**2)
if bmi<18.5:
    print("underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi>=25 and bmi<30:
    print("Overweight")
else:
    print("Obese")