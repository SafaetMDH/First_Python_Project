
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("<__Welcome to Python Pizza Deliveries! __>")

size = input("What size pizza you want? S, M, or L ")
extra_pepperoni = input("Do you want extra pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0


if size == "S":
    bill = 15

    if extra_cheese == "Y":
        bill = bill+2

    elif extra_pepperoni == "Y":
        bill = bill+1

    print(f"Your bill is ${bill}")


elif size == "M":
    bill = 25
    print(f"Your bill is ${bill}")

elif size == "L":
    bill = 25
    print(f"Your bill is ${bill}")