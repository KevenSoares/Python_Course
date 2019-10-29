"""
Exercise

8 - Make a program that asks how much you earn per hour and the number of hours worked in the month.
    Calculate and show your total salary for that month.

"""
PricePerHour = float(input("Enter your hour/work price: "))
WorkHours = float(input("Enter how many hour you've worked this month: "))

print(f'Your salary is {PricePerHour*WorkHours} R$')
