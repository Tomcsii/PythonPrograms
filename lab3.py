import random
print("---- Lab 3 ----")
print("Name: Tamas Borbely")

# Task 1
print("\n---- Task 1: Simple order ----")
print("**Select menu item**\n(1) Coke [$1.00]\n(2) Dosa [$2.50]\n(3) Pizza [$2.25]\n(4) Taco [$1.50]\n(5) Tea [$1.00]")
item_input = int(input("Selection: "))

if item_input == 1:
    amount = 1.00
elif item_input == 2:
    amount = 2.50
elif item_input == 3:
    amount = 2.25
elif item_input == 4:
    amount = 1.50
elif item_input == 5:
    amount = 1.00
else:
    amount = 0
    print("Invalid selection - setting amount to $0")

print("**Discount**\n(C) Child [under 18] (50% discount)\n(A) Adult [18-64]\n(S) Senior [65+] (25% discount)")
discount_input = input("Selection age: ")

if discount_input == "C" or discount_input == "c":
    discount = amount * 0.50
elif discount_input == "A" or discount_input == "a":
    discount = 0.00
elif discount_input == "S" or discount_input == "s":
    discount = amount * 0.25
else:
    discount = amount * -0.25
    print("\'" + discount_input + "\' is an invalid selection! Extra charge for you!")

total = (amount - discount)

print(f"Amount   $ {amount:.2f}")
print(f"Discount $ {discount:.2f}")
print("------------------")
print(f"Total    $ {total:.2f}")

# Task 2
print("\n---- Task 2: Draw circle ----")
radius = True

while radius:
    radius_input = int(input("Input size between 1-10: "))

    if radius_input >= 1 and radius_input <= 10:
        for y in range(-10, 11):
            out = ""

            for x in range(-10, 11):
                if ((x ** 2) + (y **2)) <= (radius_input **2):
                    out = out + "*"
                else:
                    out = out + "."

            print(out)

        radius = False

# task 3
print("\n---- Task 3: Dice pair expected value ----")
want_play = True

while want_play:
    n = int(input("Roll how many times? "))
    avg = 0

    for i in range(n):
        play_again = True
        numb1 = random.randint(1,6)
        numb2 = random.randint(1,6)
        sum = numb1 + numb2
        avg = avg + sum
        print(f"[{numb1}]   [{numb2}] -- {sum:2} Roll {i + 1}")
    print(f"Average dice pair value: {(avg/n):.2f}")

    while play_again:
        try_again = input("Try again [Y/N]? ")

        if try_again == "Y" or try_again == "y":
            want_play = True
            play_again = False
            
        elif try_again == "N" or try_again == "n":
            want_play = False
            play_again = False
# task 4
print("\n---- Task 4: Compute PI ----")
M = int(input("Input number of terms, M: "))
sum = 0

for n in range(0, M+1):
    denominator = (-1) ** n
    numerator = 2 * n + 1
    term = (denominator/numerator)
    sum += term
    print(f"n={n} . . . adding fraction: {denominator}/{numerator}\n   our pi = {(sum*4):.12f}\n   real pi = 3.14159265359")

# pause program until enter is pressed
print("\n---- Lab 3 Done ----")
input("Press enter to exit.")
