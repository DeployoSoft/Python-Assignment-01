# Write a program to check if a number is within a specified range.
num = int(input("Enter a number: "))
low = int(input("Enter lower bound: "))
high = int(input("Enter upper bound: "))
if low <= num <= high:
    print("The number is within the range.")
else:
    print("The number is out of range.")
