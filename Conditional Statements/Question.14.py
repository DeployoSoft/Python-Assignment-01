# Check if a year input by the user is a century year.
year = int(input("Enter a year: "))
if year % 100 == 0:
    print("Century year")
else:
    print("Not a century year")
