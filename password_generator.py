import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

l = [0] * nr_letters
s = [0] * nr_symbols
n = [0] * nr_numbers
for i in range (0,nr_letters):
    l[i] = letters[random.randint(0,25)]
for i in range (0,nr_symbols):
    s[i] = symbols[random.randint(0,8)]
for i in range (0,nr_numbers):
    n[i] = numbers[random.randint(0,9)]
password=""
pass_set = l + s + n
print("In order password:")
for i in pass_set:
    password+=str(i)
print(password)

pass_list = list(pass_set)
random.shuffle(pass_list)
print("Out of order password:")
password=""
for i in pass_list:
    password+=str(i)
print(password)