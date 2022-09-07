# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi= weight/(height**2)
bmi=round(bmi,1)
if bmi<18.5:
    print("fYour BMI is {bmi},you are Under Weight")
elif bmi<24.9:
    print(f"Your BMI is {bmi},you are Normal Weight")
elif bmi<29.9:
    print(f"Your BMI is {bmi},you are Slightly overWeight")
elif bmi<35:
    print(f"Your BMI is {bmi},you are OBESE")
else:
    print(f"Your BMI is {bmi},you are Critically Obese")
    

