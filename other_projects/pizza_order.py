print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0
pepperoni_split = ""
cheese_split = ""
size_split = ""
if size == "S":
    bill += 15
    size_split = "You choose size S that costs $15"
    if add_pepperoni == "Y":
        bill += 2
        pepperoni_split = "You choose pepperoni that costs $2"
    if extra_cheese == "Y":
        bill += 1
        cheese_split = "You choose extra cheese that costs $1"
elif size == "M":
    bill += 20
    size_split = "You choose size M that costs $20"
    if add_pepperoni == "Y":
        bill += 3
        pepperoni_split = "You choose pepperoni that costs $3"
    if extra_cheese == "Y":
        bill += 1
        cheese_split = "You choose extra cheese that costs $1"
elif size == "L":
    bill += 25
    size_split = "You choose size L that costs $25"
    if add_pepperoni == "Y":
        bill += 3
        pepperoni_split = "You choose pepperoni that costs $3"
    if extra_cheese == "Y":
        bill += 1
        cheese_split = "You choose extra cheese that costs $1"
else:
    print("Wrong input")
print(f"Your final bill is: ${bill}.\nBill split:\n{size_split}\n{pepperoni_split}\n{cheese_split}")
