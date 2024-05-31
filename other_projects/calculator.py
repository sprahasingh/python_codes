def calculate(float_first_num, float_second_num, str_operator):
    """This function is used to perform operations between two numbers"""
    ans = 0
    if str_operator == '+':
        ans = float_first_num + float_second_num
        return ans
    elif str_operator == '-':
        ans = float_first_num - float_second_num
        return ans
    elif str_operator == '*':
        ans = float_first_num * float_second_num
        return ans
    elif str_operator == '/':
        if float_second_num == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        ans = float_first_num / float_second_num
        return ans
    print(f"{float_first_num} {str_operator} {float_second_num} = {ans}")


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
        answer = round(calculate(first_num, second_num, operator), 2)
        print(answer)
        while True:
            flag = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, type "
                         f"'exit' to exit\n")
            if flag not in {'y', 'n', 'exit'}:
                print("Invalid input")
                continue
            elif flag == 'exit':
                exit()
            else:
                break
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        continue
