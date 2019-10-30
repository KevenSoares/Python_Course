"""
Exercises

16 - Make a program for a paint store. The program should request the size in square meters of the area to be painted.
 Consider that the ink coverage is 1 liter per 3 square meters and that the ink is sold in 18 liter cans, which cost
 $ 80.00. Inform the user of the quantities of paint cans to be purchased and the total price.

"""
import math

area = float(input("Enter the area: "))
ink = area/3
cost = math.ceil(ink/18)*80.00
print(f"you need {math.ceil(ink/18)} ink cans and the cost is: {cost} R$")
