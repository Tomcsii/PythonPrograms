import random

# Print info
def print_lab_info():
    print("---- Lab 5 ----")
    print("Name: Tamas Borbely")

def task0():
  # Example of calling a function from taskX() functions.
  # you should write all functions "outside" your task1()-task4() functions.
  print_lab_info()

def input_list():
    user_input = 0
    list_input = []

    while user_input > -1:
        user_input = int(input("Input positive int: "))

        if user_input > -1:
            list_input.append(user_input)
    return list_input     

def compute_average(aList):

    if len(aList) == 0:
        return 0.0 
    else:
        avg = 0

        for i in range(len(aList)):
            avg += aList[i]
        avg /= len(aList)
        return avg

def task1():
    YN = "Y"

    while YN == "Y":
        user_list = input_list()
        list_average = compute_average(user_list)
        print(f"List average {list_average:.2f}")
        YN = input("Do again [Y/N]? ").upper()

def task2():
    string_input = str(input("Input a long string: ")).upper()
    input_list = list(string_input)
    input_set = set(string_input)
    empty_dict = {}
    
    for items in input_set:
        empty_dict.update({items:0})

    for i in range(len(input_list)):

        if input_list[i] in empty_dict.keys():
            empty_dict[input_list[i]] += 1

    star = "*"
    for key in empty_dict:
        print(f"\'{key}\' |{(empty_dict[key])*star}")

def task3():
    encoder = {'A': '$', 'B': 'F', 'C': 'C', 'D': '2', 'E': 'B', 'F': 'I', 'G': '=', 'H': '*', 'I': '"', 'J': ']', 'K': '1',
     'L': '0', 'M': '@', 'N': '[', 'O': 'L', 'P': '%', 'Q': '&', 'R': '(', 'S': 'G', 'T': 'K', 'U': '5', 'V': '!',
     'W': '^', 'X': '+', 'Y': '6', 'Z': '-', '1': 'H', '2': 'A', '3': 'J', '4': '7', '5': '4', '6': 'D', '7': 'E',
     '8': '9', '9': ')', '0': ';', ',': '3', '.': '/', ' ':'_'}
    decoder = {'$': 'A', 'F': 'B', 'C': 'C', '2': 'D', 'B': 'E', 'I': 'F', '=': 'G', '*': 'H', '"': 'I', ']': 'J', '1': 'K',
     '0': 'L', '@': 'M', '[': 'N', 'L': 'O', '%': 'P', '&': 'Q', '(': 'R', 'G': 'S', 'K': 'T', '5': 'U', '!': 'V',
     '^': 'W', '+': 'X', '6': 'Y', '-': 'Z', 'H': '1', 'A': '2', 'J': '3', '7': '4', '4': '5', 'D': '6', 'E': '7',
     '9': '8', ')': '9', ';': '0', '3': ',', '/': '.', '_': ' '}
    YN = "Y"

    while YN == "Y":
        string_input = str(input("Input message: ")).upper()
        e_or_d = str(input("Encode (E) or Decode (D)? ")).upper()

        if e_or_d == "E":
            list_encode = list(string_input)

            for i in range(len(list_encode)):
                print(f"{encoder[list_encode[i]]}", end="")
            print()
        elif e_or_d == "D":
            list_decode = list(string_input)

            for i in range(len(list_decode)):
                print(f"{decoder[list_decode[i]]}", end="")
            print()
        YN = str(input("Encode/decode again [Y/N]? ")).upper() 

def random_set():
    random_set = {}
    random_set = set()

    while len(random_set) < 5:
        random_num = random.randint(1,20)

        if random_num in random_set:
            None
        else:
            random_set.add(random_num)

    return random_set

def print_set(aSet, prompt=""):
    print(prompt, end="")

    for item in aSet:
        print(f"{item} ", end="")
    print()

def task4():
    YN = "Y"

    while YN == "Y":
        user_set = {}
        user_set = set()

        while len(user_set) != 5:
            number_inputs = input("Enter 5 numbers between 1 - 20: ")
            user_set = set(number_inputs)
            user_set.remove(" ")

        computer_set = random_set()
        print_set(computer_set, "Computer's numbers: ")

        for items in user_set:
            user_set.add(int(items))

            if type(items) == str:
                user_set.remove(items)
        
        combined_set = user_set.intersection(computer_set)

        if len(combined_set) == 0:
            print("NO MATCHES!!")

        elif len(combined_set) > 0:
            print(f"{len(combined_set)} matches found: ", end="")

            for item in combined_set:
                print(f"{item} ", end="")
            print()

            if len(combined_set) == 5:
                print(f"YOU WIN!")

        YN = str(input("Try again [Y/N]? ")).upper()
    
def main():
    ### Don't forget to update print_lab_info() function
    task0()

    print("\n---- Task 1: List average ----")
    task1()

    print("\n---- Task 2: Character count graph ----")
    task2()

    print("\n---- Task 3: Encoder/decoder ----")
    task3()

    print("\n---- Task 4: Lotto LESS ----")
    task4()

if __name__ == "__main__":
    main()