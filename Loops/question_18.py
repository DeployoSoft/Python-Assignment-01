# Use a loop to print numbers in reverse order within a given range.
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
for i in range(end, start - 1, -1):
    print(i)
