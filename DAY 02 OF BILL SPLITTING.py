#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator! ")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of Tip you want to give? 10,12,15? "))
x=round(((total_bill/100)*tip),2)
total_bill += x
spilt = int(input("among how many persons you want to split the bill ?"))
total_bill /=spilt
total_bill ="{:.2f}".format(total_bill)
print(f"Each person should pay : $ {total_bill}")

