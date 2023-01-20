print("-----< WELCOME TO THE ROLER COASTER >-----")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride!")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 7
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo ? Y/N ")
    if wants_photo == "Y":
        bill = bill+3
    print(f"Your bill is ${bill}")

else:
    print("You can not ride")