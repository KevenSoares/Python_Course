"""
Exercises

03 - Make a program that checks whether a letter you type is "F" or "M".
     As the lyrics read: F - Female, M - Male, Invalid Sex.

"""
g = input("Type the gender: ")
if g == 'M'or g == 'm':
    print("Male")
elif g == 'F' or g == 'f':
    print("Female")
else:
    print("Invalid Sex")
