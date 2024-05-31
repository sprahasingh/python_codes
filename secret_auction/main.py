import clear
import art

print(art.logo)
print("Welcome to the secret auction program.")
auction = {}
max_bid = 0
draw = 0
max_bid_holder = ''
while True:
    name = input("What is your name?\n")
    bid = int(input("What is your bid\n"))
    auction[name] = bid
    flag = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if flag not in {'yes', 'no'}:
        print("Invalid input")
        continue
    if flag == 'no':
        for i in auction:
            if auction[i] == max_bid:
                draw = 1
            elif auction[i] > max_bid:
                max_bid = auction[i]
                max_bid_holder = i
                draw = 0
        if draw == 1:
            print("Two or more people have same maximum bid. Try again!")
            while True:
                again = input("Press 'yes' to start again, Press 'no' to exit\n")
                if again not in {'yes', 'no'}:
                    print("Invalid input")
                    continue
                if again == 'yes':
                    break
                else:
                    exit()
        else:
            print(f"The winner is {max_bid_holder} with a bid of {max_bid}")
            exit()
        if again == 'yes':
            clear.clear_console()
            continue
    else:
        clear.clear_console()
