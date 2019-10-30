"""
Exercises

05 - Make a program for reading a student's two partial notes. The program should calculate the average achieved per
     student and present:
        05.1 - The message "Approved" if the average achieved is greater than or equal to seven;
        05.2 - The message "Disapproved" if the average is less than seven;
        05.3 - The message "Approved with Distinction" if the average is ten.

"""
n1 = float(input("1st Grade: "))
n2 = float(input("2nd grade: "))
ave = (n1+n2)/2
if 7 <= ave < 10:
    print("Approved")
elif ave == 10:
    print("Approved with Distinction")
else:
    print("Disapproved")
