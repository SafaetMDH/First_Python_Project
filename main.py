
# This is how its working out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400

print("---< Welcome to Leap Year Calculator >---")

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    print("Leap year.")
elif year % 100 == 0:
    print("Leap year.")
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")