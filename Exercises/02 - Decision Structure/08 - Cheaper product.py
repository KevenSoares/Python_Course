"""
Exercises:

8 - Make a program that asks for the price of three products and tells you which product to buy,
knowing that the decision is always for the cheapest.

"""


n1 = float(input("Enter the 1st product price: "))
n2 = float(input("Enter the 2nd product price: "))
n3 = float(input("Enter the 3th product price: "))

if n1 < n2 < n3 or n1 < n3 < n2:
    print(f'you should buy product 1, that costs: {"%.2f"%n1} R$')
elif n2 < n1 < n3 or n2 < n3 < n1:
    print(f"you should buy product 2, that costs: {'%.2f'%n2} R$")
else:
    print(f"you should buy product 3, that costs: {'%.2f'%n3} R$")
