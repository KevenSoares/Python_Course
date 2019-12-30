"""
Exercises:

9 - Make a program that reads three numbers and shows them in descending order.

"""


n1 = float(input("Enter the 1st number: "))
n2 = float(input("Enter the 2nd number: "))
n3 = float(input("Enter the 3th number: "))

if n1 > n2 > n3:
    print(f"{n1},{n2},{n3}")
elif n1 > n3 > n2:
    print(f"{n1},{n3},{n2}")
elif n2 > n1 > n3:
    print(f"{n2},{n1},{n3}")
elif n2 > n3 > n1:
    print(f"{n2},{n3},{n1}")
else:
    if n1 > n2:
        print(f"{n3},{n1},{n2}")
    else:
        print(f"{n3},{n2},{n1}")
