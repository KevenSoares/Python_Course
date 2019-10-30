"""
Exercise

14 - John the Fisherman, a good man, bought a microcomputer to control the daily income of his work.
     Every time he brings a fish weight higher than that established by the fishing regulation of the
    state of São Paulo (50 kilos) must pay a fine of $ 4.00 per excess kilo. John needs you to make a
    program that reads the weight variable (fish weight) and calculates the excess. Record in the excess
    variable the amount of pounds over the limit and in the fine variable the amount of the fine that John must pay.
    Print the program data with the appropriate messages.

"""

weight = float(input("Enter the fish weight: "))
excess = weight-50
fine = excess*4
print(f"""The fish's weight is {weight} kg, the excess is {excess} kg, and the fine is {fine} R$""")
