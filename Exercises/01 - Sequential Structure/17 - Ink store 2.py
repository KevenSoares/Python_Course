"""
Exercises

17 - Make a program for a paint store. The program should request the size in square meters of the area to be painted.
Consider that the ink coverage is 1 liter per 6 square meters and that the ink is sold in 18 liter cans, which cost
$ 80.00 or 3.6 liter gallons, which cost $ 25.00.Inform the user of the quantities of paint to be purchased and their
prices in 3 situations:
17.1 - buy only 18 liter cans;
17.2 - buy only 3.6 gallon gallons;
17.3 - mix cans and gallons so that the price is the lowest. Add 10% off and always round the values
       up, ie consider full cans.

"""

import math

area = float(input("Enter the area: "))
ink = area/6
costCan = math.ceil(ink/18)*80.00
costGallon = math.ceil(ink/3.6)*25.00

restOfArea1 = ink % 18
restOfArea2 = ink % 3.6

alternativeCost1 = (math.ceil(restOfArea1/3.6))*25.00 + math.ceil((ink - restOfArea1)/18)*80.00
alternativeCost2 = (math.ceil(restOfArea2/18))*80.00 + math.ceil((ink - restOfArea2)/3.6)*25.00

print(f"you need {math.ceil(ink/18)} ink cans or {math.ceil(ink/3.6)} ink gallons")
print(f'The cost of cans is: {costCan} R$\nThe cost of gallons is {costGallon}R$')

print(f'you can also use {(ink - restOfArea1)/18} cans + {(math.ceil(restOfArea1/3.6))} gallons')
print(f'The price is: {alternativeCost1}')

print(f'or {math.ceil((ink - restOfArea2)/3.6)} gallons + {(math.ceil(restOfArea2/18))} cans')
print(f'The price is: {alternativeCost2}')
