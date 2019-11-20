"""
Exercises

07 - Make a Program that reads three numbers and shows the largest and smallest of them.

"""

n1 = float(input("Enter the 1st number: "))
n2 = float(input("Enter the 2nd number: "))
n3 = float(input("Enter the 3th number: "))

if n1 > n2 > n3:
    print(f"the greater is: {n1}")
    print(f"the smaller is: {n3}")
elif n1 > n3 > n2:
    print(f"the greater is: {n1}")
    print(f"the smaller is: {n2}")
elif n2 > n1 > n3:
    print(f"the greater is: {n2}")
    print(f"the smaller is: {n3}")
elif n2 > n3 > n1:
    print(f"the greater is: {n2}")
    print(f"the smaller is: {n1}")
else:
    print(f"the greater is: {n3}")
    if n1 > n2:
        print(f"the smaller is: {n2}")
    else:
        print(f"the smaller is: {n1}")


