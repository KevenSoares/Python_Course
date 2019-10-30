""""
Exercises
15 - Make a program that asks how much you earn per hour and the number of hours worked in the month.
Calculate and show your total salary for that month, knowing that 11% is deducted for Income Tax, 8%
for INSS and 5% for the union, make a program that gives us:
15.1 - gross salary.
15.2 - how much you paid to the INSS.
15.3 - how much you paid the union.
15.4 - the net salary.
15.5 - calculate discounts and net salary as shown in the table below:
15.5.1 - + Gross Salary: R$
15.5.2 - IR (11%): R$
15.5.3 - INSS (8%): ​​R$
15.5.4 - Union (5%): R$
15.5.6 = Net Salary: R$

"""

PricePerHour = float(input("Enter your hour/work price: "))
WorkHours = float(input("Enter how many hour you've worked this month: "))
salary = PricePerHour*WorkHours
print(f'Your salary is: \n+{salary} R$\n-IR: {salary*0.11} R$\n-INSS: {salary*0.08} R$\n-Union: {salary*0.05} R$\n=Net'
      f'salary: {salary-salary*0.11-salary*0.08-salary*0.05} R$')

