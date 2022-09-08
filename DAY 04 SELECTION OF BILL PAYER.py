import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

last_index=len(names)
bill_payer=random.randint(0,last_index-1)
print(names[bill_payer]+" is going to buy the meal today! ")

#another easy way is to use choice

#bill_payer=random.choice(names)
#print(bill_payer+" is going to buy the meal today! ")

