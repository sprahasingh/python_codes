def calculate(first_num,second_num,operator):
    """This function is used to perform operations between two numbers"""
    ans = 0
    if operator == '+':
        ans = first_num + second_num
        return ans
    elif operator == '-':
        ans = first_num - second_num
        return ans
    elif operator == '*':
        ans = first_num * second_num
        return ans
    elif operator == '/':
        if second_num == 0 :
            raise ZeroDivisionError("Division by zero is not allowed")
        ans = first_num / second_num
        return ans
    print(f"{first_num} {operator} {second_num} = {ans}")
flag = 'n'
answer = 0
while True:
    if flag == 'y':
        first_num = answer
    else:
        first_num = float(input("Enter first number\n"))
    second_num = float(input("Enter second number\n"))
    operator = input("Enter operator from '+', '-', '*', '/'\n")
    if operator not in {'+', '-', '*', '/'}:
        print("Enter valid operator. Please use +, -, *, or /.")
        continue
    try:
        answer = round(calculate(first_num,second_num,operator),2)
        print(answer)
        while True:
            flag = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, type 'exit' to exit\n")
            if flag not in {'y', 'n','exit'}:
                print("Invalid input")
                continue
            elif flag == 'exit':
                exit()
            else:
                break
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        continue
        