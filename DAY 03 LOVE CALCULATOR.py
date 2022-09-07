# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


lower_case1=name1.lower()+name2.lower()

#time for Letter TRUE
TRUE=lower_case1.count("t") + lower_case1.count("r") + lower_case1.count("u") + lower_case1.count("e")

#now time for Letter Love
LOVE=lower_case1.count("l") + lower_case1.count("o") + lower_case1.count("v") + lower_case1.count("e")


total = str(TRUE) + str(LOVE)
total=int(total)
if total<=10 or total >=90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total>=40 and total<=50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")


