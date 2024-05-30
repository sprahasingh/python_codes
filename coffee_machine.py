def coffee_machine(available, profit) :
    menu = [{'name' : 'espresso', 'ingredients' : {'water' : 50, 'milk' : 0, 'coffee' : 18},'cost' : 1.50 },
            {'name' : 'latte', 'ingredients' : {'water' : 200, 'milk' : 150, 'coffee' : 24},'cost' : 2.50 },
            {'name' : 'cappuccino', 'ingredients' : {'water' : 250, 'milk' : 100, 'coffee' : 24},'cost' : 3.00 }]
    coffee_names = []
    for coffee in menu :
        coffee_names.append(coffee['name'])
    def fetch_coffee_detail(coffee_type) :
        for detail in menu :
            if detail['name'] == coffee_type :
                return detail
    def print_report() :
        print(f"Water: {available['water']}ml\nMilk: {available['milk']}ml\nCoffee: {available['coffee']}g\nMoney: ${profit}")
    def take_money(money_type) :
        while True:
            money = input(f"Pay {money_type}: ")
            try :
                money_value = float(money)
                return money_value
            except :
                print("Enter valid input")
                continue
    def check_money(coffee_detail,money_paid) :
        if money_paid >= coffee_detail['cost'] :
            return True
        else :
            return False
    def make_coffee(available, profit, coffee_detail) :
        for i in available :
            available[i]-=coffee_detail['ingredients'][i]
        profit += coffee_detail['cost']
        return available['water'], available['milk'], available['coffee'], profit
    def calculate_money(quarters, dimes, nickels, pennies) :
        return quarters*0.25+dimes*0.10+nickels*0.05+pennies*0.01
    def check_requirement(available, coffee_detail) :
        for i in available :
            if available[i] < coffee_detail['ingredients'][i] :
                print(f"Sorry there is not enough {i}.")
                return False
        return True


    while True :
        while True:
            coffee_type = input("“What would you like? (espresso/latte/cappuccino):\n").lower()
            coffee_detail = {}
            if coffee_type in coffee_names :
                coffee_detail = fetch_coffee_detail(coffee_type)
                break
            elif coffee_type in {'off','report'} :
                break
            else :
                print("Enter valid input")
                continue
        if coffee_type == 'off' :
            exit()
        elif coffee_type == 'report' :
            print_report()
            continue
        elif check_requirement(available, coffee_detail) :
            print(f"Please pay ${coffee_detail['cost']}")
            quarters = take_money('quarters')
            dimes = take_money('dimes')
            nickels = take_money('nickels')
            pennies = take_money('pennies')
            money_paid = round((calculate_money(quarters,dimes,nickels,pennies)),2)
            if check_money(coffee_detail,money_paid) :
                print(f"Total money paid: ${money_paid}")
                change = round((money_paid - coffee_detail['cost']),2)
                print(f"Enjoy your {coffee_detail['name']}!!")
                if change > 0 :
                    print(f"Here's your change of ${change}")
            else :
                print("Sorry that's not enough money. Money refunded.")

            available['water'], available['milk'], available['coffee'], profit = make_coffee(available, profit, coffee_detail)
initial_available = {'water' : 1000, 'milk' : 500, 'coffee' : 100}
initial_profit = 0
coffee_machine(initial_available, initial_profit)