def coffee_machine(water,milk,coffee,money) :
    machine = 'on'
    espresso = {'name' : 'espresso', 'water' : 50, 'milk' : 0, 'coffee' : 18, 'money' : 1.50}
    latte = {'name' : 'latte', 'water' : 200, 'milk' : 150, 'coffee' : 24, 'money' : 2.50}
    cappuccino = {'name' : 'cappuccino', 'water' : 250, 'milk' : 100, 'coffee' : 24, 'money' : 3.00}
    def convert(type) :
        if type == 'espresso' :
            return espresso
        elif type == 'latte' :
            return latte
        elif type == 'cappuccino' :
            return cappuccino
    def print_report() :
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    def take_money(money_type) :
        while True:
            money = input(f"Pay {money_type}: ")
            try :
                money_value = float(money)
                return money_value
            except :
                print("Enter valid input")
                continue
    def check_money(coffee_type,money_paid) :
        if money_paid >= coffee_type['money'] :
            return True
        else :
            return False
    def make_coffee(water, milk, coffee, money, coffee_type) :
        water-=coffee_type['water']
        milk-=coffee_type['milk']
        coffee-=coffee_type['coffee']
        money+=coffee_type['money']
        return water, milk, coffee, money
    def calculate_money(quarters, dimes, nickels, pennies) :
        return quarters*0.25+dimes*0.10+nickels*0.05+pennies*0.01
    def check_requirement(water, milk, coffee, coffee_type) :
        if water < coffee_type['water'] :
            print("Sorry there is not enough water.")
            return False
        elif milk < coffee_type['milk'] :
            print("Sorry there is not enough milk.")
            return False
        elif coffee < coffee_type['coffee'] :
            print("Sorry there is not enough coffee.")
            return False
        else :
            return True
    while machine == 'on' :
        while True:
            type = input("“What would you like? (espresso/latte/cappuccino):\n").lower()
            if type in {'espresso','latte','cappuccino'} :
                coffee_type = convert(type)
                break
            elif type in {'off','report'} :
                break
            else :
                print("Enter valid input")
                continue
        if type == 'off' :
            exit()
        elif type == 'report' :
            print_report()
            continue
        elif check_requirement(water, milk, coffee, coffee_type) :
            print(f"Please pay ${coffee_type['money']}")
            quarters = take_money('quarters')
            dimes = take_money('dimes')
            nickels = take_money('nickels')
            pennies = take_money('pennies')
            money_paid = round((calculate_money(quarters,dimes,nickels,pennies)),2)
            if check_money(coffee_type,money_paid) :
                print(f"Total money paid: ${money_paid}")
                change = round((money_paid - coffee_type['money']),2)
                print(f"Enjoy your {coffee_type['name']}!!")
                if change > 0 :
                    print(f"Here's your change of ${change}")
            else :
                print("Sorry that's not enough money. Money refunded.")

            water, milk, coffee, money = make_coffee(water, milk, coffee, money, coffee_type)
coffee_machine(1000,500,100,0)