def is_leap(int_year):
    if int_year % 4 == 0:
        if int_year % 100 == 0:
            if int_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(int_year, int_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(int_year) and int_month == 2:
        return 29
    else:
        return month_days[int_month - 1]


year = int(input("Enter year\n"))
month = int(input("Enter month number\n"))
if not 1 <= month <= 12:
    print("Enter valid month number")
    exit()
days = days_in_month(year, month)
print(days)
