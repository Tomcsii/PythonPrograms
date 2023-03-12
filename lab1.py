# Please fill out your info for each lab
print("---- Lab 1 ----")
print("Name: Tamas Borbely")

# Task 1
print('\n---- Task 1: Currency converter ----')
cur_cad = float(input("Amount in Canadian Dollars: "))
print("Amount in other currencies: ")
print("USD: " + str(cur_cad * 0.76))
print("EUR: " + str(cur_cad * 0.75))
print("NGN: " + str(cur_cad * 322.24))
print("CNY: " + str(cur_cad * 5.25))
print("INR: " + str(cur_cad * 97.14))


# Task 2
print('\n---- Task 2: String math ----')

print("enter 3 strings")
str1 = input("str1: ")
str2 = input("str2: ")
str3 = input("str3: ")
print("String conatacentaion")
print("str1 + str2 + str3 = " + str(str1) + str(str2) + str(str3))
print("str3+ str2 + str1 = " + str(str3) + str(str2) + str(str1))
print("str2 + str1 + str3 = " + str(str2) + str(str1) + str(str3))
ipt = int(input("Input an integer: "))

print("String multiply: ")
print("num x str1 = " + (ipt * str1))
print("num x str2+str3 = " + (ipt * (str2 + str3)))


# Task 3
print("\n---- Task 3: Math operators ----")

intx = int(input("Input integer x: "))
inty = int(input("Input integer y: "))
print("Integer math: ")
print("x / y = " + str(intx/inty))
print("x// y = " + str(intx//inty))
print("x % y = " + str(intx%inty))
print("x** y = " + str(intx**inty))
fltx = float(input("Input float x: "))
flty = float(input("Input float y: "))
print("Float math: ")
print("x / y = " + str(fltx/flty))
print("x// y = " + str(fltx//flty))
print("x % y = " + str(fltx%flty))
print("x** y = " + str(fltx**flty))


# Task 4
print('\n---- Task 4: Simple cylinder computation ----')

pi = 355/113
rad = int(input("Radius: "))
hgt = int(input("Height: "))

sa = ((2 * pi * rad * hgt) + (2*pi*(rad**2)))
vol = (pi * (rad**2) * hgt)

print("Cylinder surface area:" + str(sa))
print("Cylinder volume: " + str(vol))

## Adding the final "input" causes python to wait on the user to press enter
## before exiting the program.
print("\n---- FINISHED ----")
input("Press enter to end.")