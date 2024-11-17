# Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).
grade = float(input("Enter your grade percentage: "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
