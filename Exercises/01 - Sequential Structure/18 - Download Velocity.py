"""
Exercises

18 - Make a program that asks for the size of a downloadable file (in MB) and the speed of an Internet link (in Mbps),
     calculate and enter the approximate file download time using this link (in minutes).

"""
import math

fileSize = int(input("Enter the size of the file(MB): "))
internetVelocity = int(input("Enter the internet velocity(Mbps): "))
timeOfDownload = (fileSize/(internetVelocity*60))
print(f"Estimated time: {timeOfDownload} minute(s)")




