import calendar
def get_month_number(month_name):
    month_name = month_name.capitalize()
    if month_name in calendar.month_name:
        return list(calendar.month_name).index(month_name)
    else:
        return None
user_input = input("Enter the month and year : ")
if ',' not in user_input:
    print(" Please enter the input in the format: MonthName, Year ")
else:
    parts = user_input.split(',')
    if len(parts) != 2:
        print("Incorrect input format. Make sure to use a comma between month and year.")
    else:
        month_str = parts[0].strip()
        year_str = parts[1].strip()
        month_num = get_month_number(month_str)
        if month_num is None or month_num == 0:
            print("Please enter a valid month")
        else:
            if not year_str.isdigit():
                print("Year must be a number")
            else:
                year = int(year_str)
                print("\nHere is the calendar:\n")
                print(calendar.month(year, month_num))
