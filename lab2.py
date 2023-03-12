# Please fill out your info for each lab
print("---- Lab 2 ----")
print("Name: Tamas Borbely")

# Task 1
print("\n---- Task 1: Three year investment return ----")
usrname = input("Name: ").title()
strpusr = usrname.strip()
intlAmt = float(input("Initial amount: $ "))
rtofrtrn = float(input("Rate of Return: % "))
prcnt = rtofrtrn/100
usrname = usrname.title()


year1new = intlAmt + intlAmt * prcnt
year2new = year1new + year1new * prcnt
year3new = year2new + year2new * prcnt

print(f"Client: {usrname}, yearly rate of return multiplier: {prcnt:.2f}")
print(f"Year 1      Starting amount: $ {intlAmt:8.2f}           Ending amount: $ {year1new:8.2f}")
print(f"Year 1      Starting amount: $ {year1new:8.2f}           Ending amount: $ {year2new:8.2f}")
print(f"Year 1      Starting amount: $ {year2new:8.2f}           Ending amount: $ {year3new:8.2f}")

# Task 2
print("\n----Task 2 Leetspeak converter ----")
usrinput = input("Type a long string: ")
usrinput = usrinput.upper()
usrinput = usrinput.replace("T", "7").replace("A", "^").replace("E", "3").replace("I", "!").replace("B", "8").replace("O", ".").replace("C", "<").replace("S", "$")
print(usrinput)

# task 3
print("\n---- Task 3: Substring highlighter ----")
sntncinpt = input("Type a sentance at the prompt below:\n> ")
sbstrnginpt = input("Enter a substring below to highlight:\n> ")
stnclen = int(len(sntncinpt))
sbstrnglen = int(len(sbstrnginpt))
print(f"Sentance has {stnclen} characters, susbtring has {sbstrnglen} characters.")
start = 0
end = stnclen
hm = int(sntncinpt.find(sbstrnginpt))
hm2 = int(hm + sbstrnglen)
sliced = sbstrnginpt.upper()
print(sntncinpt[0:hm] + "*" + sliced + "*" + sntncinpt[hm2:end])


# task 4
print("\n---- Task 4: Exponent ----")
lab4 = input("Input exponent in the form x^y: ")
firstnum = int(lab4[0])
secondnum = int(lab4[2])
awns = firstnum ** secondnum

print("Extracted numbers " + str(firstnum) + " " + str(secondnum))
print(lab4 + " = " + str(awns))

# pause program until enter is pressed
print("\n---- Lab 2 Done ----")
input("Press enter to exit.")
