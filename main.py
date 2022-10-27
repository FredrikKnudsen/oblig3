from function import isLeapYear

print("Leap year check!\nWhat year do you want to check? ")

year = int(input())
if isLeapYear(year):
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")
