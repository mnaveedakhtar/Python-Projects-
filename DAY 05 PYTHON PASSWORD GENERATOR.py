#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=""

for char in range(0,nr_letters):
    random_char=random.choice(letters)
    password+=random_char

for char in range(0,nr_symbols):
    random_char=random.choice(numbers)
    password += random_char

for char in range(0,nr_numbers):
    random_char=random.choice(symbols)
    password += random_char


print(password)

#*************************METHOD 2******************************#
print("HERE IS A 2ND METHOD:\n")
password_list=[]

for char in range(0,nr_letters):
    random_char=random.choice(letters)
    password_list +=random_char

for char in range(0,nr_symbols):
    random_char=random.choice(numbers)
    password_list += random_char

for char in range(0,nr_numbers):
    random_char=random.choice(symbols)
    password_list += random_char

random.shuffle(password_list)


random_password=""
for char in password_list:
    random_password += char
    
print(f"YOUR PASSWORD IS: "+ random_password)
