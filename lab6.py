import random

def print_student_info():
    print("Name: Tamas Borbely")

def task0():
    print_student_info()

# Functions for task 1
# Write the function average_num() outside your task1() function.

def average_num(*nums):
    if len(nums) > 0:
        total = 0
        for i in nums:
            total += i
        avg = total/int(len(nums))
        return avg
    else:
        return 0

def task1():
    YN = "Y"
    while YN == "Y":
        four_or_five = int(input(f"Input 4 or 5 numbers? "))
        if four_or_five == 4:
            list_input = list(input("Input 4 numbers [x1, x2, x3, x4]\t: ").replace(" ", "").split(","))
            x1 = int(list_input[0])
            x2 = int(list_input[1])
            x3 = int(list_input[2])
            x4 = int(list_input[3])
            input_avg = average_num(x1,x2,x3,x4)
            print(f"Average is {input_avg:.2f}")
        elif four_or_five == 5:
            list_input = list(input("Input 5 numbers [x1, x2, x3, x4, x5]\t: ").replace(" ", "").split(","))
            x1 = int(list_input[0])
            x2 = int(list_input[1])
            x3 = int(list_input[2])
            x4 = int(list_input[3])
            x5 = int(list_input[4])
            input_avg = average_num(x1,x2,x3,x4,x5)
            print(f"Average is {input_avg:.2f}")
        
        YN = input("Try again? ").upper()

# Task 2
# Write function build_stock_dict() here.
def build_stock_dict(*astring):
    empty_dict = {}
    new_list = astring[0].split()
    
    for i in range(len(new_list)):
        nice = list(new_list[i].split(":"))
        new_list.append(nice)

    for x in range(len(new_list)):  

        for i in new_list:
            if type(i) != list:
                new_list.remove(i)

    for lists in new_list:
        x = [str(lists[0]), float(lists[1])]
        empty_dict.update({lists[2]:x})

    return empty_dict


# This function is provided for you.
def print_stock_dict(stock_dict):
    keys = list(stock_dict.keys())
    print("{:10s} {:6s}  {}".format("Symbol", "Price", "Company Name"))
    print("-"*31)
    for k in keys:
        print(f"{k:7s} {stock_dict[k][1]:8.2f}   {stock_dict[k][0]}") 
        # stock_dict[k][1]
        # ^^^^^^^^^^^^^    <- this gets the list for the key k
        #              ^^^ <- this retrieves item [1] in the list (price of stock)
        #
    print() # <- an extra empty print to make it look nice


def task2():
    stock_dict1 = {"SNAP": ["Snap", 10.08], "PINS": ["Pinterest", 29.40], "GOOG": ["Google", 96.58]}
    stock_list_string = "Apple:155.74:AAPL Tesla:228.52:TSLA Ford:13.26:F Microsoft:9.12:MSFT Shopify:34.19:SHOP"
    print_stock_dict(stock_dict1)
    stock_dict2 = build_stock_dict(stock_list_string)
    print_stock_dict(stock_dict2)

# Task 3 functions create_rand_list(), delete_list_item(), print_list() here ourside task3()

def create_rand_list():
    num_of_element = random.randint(5,15)
    min_value = random.randint(5,10)
    max_value = random.randint(20,50)
    random_list = []
    while len(random_list) != num_of_element:
        random_list.append(random.randint(min_value,max_value))
    return random_list

def print_list(a_list):
    print("---list---")
    if len(a_list) == 0:
        print(f"(empty)")
    else:
        for i in a_list:
            print(f"({i})->", end="")
        print("(end)")

def delete_item_from_list(a_list, item):
    if item in a_list:
        location = a_list.index(item)
        a_list.remove(item)
        return location
    else:
        return -1

def task3():
    YN = "Y"
    random_list = create_rand_list()
    while YN == "Y":
        print_list(random_list)
        user_input = int(input("Item to delete: "))
        deleted = delete_item_from_list(random_list, user_input)
        if deleted >= 0:
            print(f"Item {user_input} successfully delted at position {deleted}.")
        else:
            print(f"Item {user_input} could not be deleted.")
        YN = input("Delete item [Y/N]? ").upper()
# Task 4
# Write functions print_image and uncompress_rle_image() here
def print_image(image):
    for items in image:
        print(f"{items}")
    

def uncompress_rle_image(rle_image):
    image = []
    for lists in rle_image:
        x = ""
        for i in range(len(lists)):
            x += lists[i][0]*lists[i][1]
        image.append(str(x))
    return image

def task4():
    rle_image1 = [[(5, '-')], [(2, ' '), (1, '|')], [(2, ' '), (1, '|')], [(1, ' '), (3, '-')]]
    rle_image2 = [[(9, ' '), (1, '.'), (1, '8'), (1, '.'), (1, ' ')], [(9, ' '), (3, '8'), (1, ' ')], [(9, ' '), (3, '8'), (1, 'l')],
     [(8, ' '), (1, 'j'), (4, '8'), (1, '.')], [(7, ' '), (1, '.'), (6, '8'), (1, '.')],
     [(6, ' '), (1, '.'), (8, '8'), (1, '.')], [(4, ' '), (1, '.'), (1, 'd'), (10, '8'), (1, 'b'), (1, '.'), (1, ' ')],
     [(2, ' '), (1, '.'), (1, 'd'), (14, '8'), (1, 'b'), (1, '.')], [(1, ' '), (1, '.'), (18, '8'), (1, 'b'), (1, '.')],
     [(1, '.'), (21, '8')], [(22, '8')], [(3, '8'), (1, 'P'), (2, '"'), (1, '4'), (3, '8')],
     [(1, '`'), (1, 'P'), (1, "'"), (5, ' '), (1, '.'), (4, ' '), (1, '.'), (5, ' '), (1, '`'), (1, 'q'), (1, "'")],
     [(1, ' '), (1, '`'), (1, '-'), (2, '.'), (4, '_'), (1, ':'), (2, ' '), (1, ':'), (4, '_'), (2, '.'), (1, '-'),
      (1, "'"), (1, ' ')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
     [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
     [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
     [(7, ' '), (1, '\\'), (1, '('), (1, '/'), (1, '\\'), (1, ')'), (1, '\\'), (1, '/'), (1, ' '), (1, 'm'), (1, 'h')]]
    rle_image3 = [[(52, '.')], [(52, '.')], [(25, '.'), (1, '/'), (1, '\\'), (25, '.')], [(18, '.'), (6, '_'), (1, '/'), (2, '_'), (1, '\\'), (7, '_'), (17, '.')], [(18, '.'), (2, '|'), (13, '-'), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (13, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '\\'), (3, '|'), (1, '/'), (4, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (3, ' '), (1, '['), (1, ' '), (1, '@'), (1, '-'), (1, '@'), (1, ' '), (1, ']'), (3, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '('), (1, ' '), (1, '.'), (1, ' '), (1, ')'), (4, ' '), (2, '|'), (7, '.'), (7, ' '), (3, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '_'), (1, '('), (1, 'O'), (1, ')'), (1, '_'), (4, ' '), (2, '|'), (7, '.'), (1, '|'), (1, 'E'), (1, 'X'), (1, 'I'), (1, 'T'), (1, ' '), (1, '|'), (3, '.')], [(18, '.'), (2, '|'), (3, ' '), (1, '/'), (1, ' '), (1, '>'), (1, '='), (1, '<'), (1, ' '), (1, '\\'), (3, ' '), (2, '|'), (7, '.'), (1, '|'), (2, '='), (2, '>'), (1, ' '), (1, '|'), (3, '.')], [(18, '.'), (2, '|'), (2, '_'), (1, '/'), (1, '_'), (1, '|'), (1, '_'), (1, ':'), (1, '_'), (1, '|'), (1, '_'), (1, '\\'), (2, '_'), (2, '|'), (17, '.')], [(18, '.'), (17, '-'), (17, '.')], [(52, '.')], [(52, '.')]]
    
    # uncomment code for task4
    print("\t\tImage 1\n")
    image1 = uncompress_rle_image(rle_image1)
    print_image(image1)
    print("\t\tImage 2\n")
    image2 = uncompress_rle_image(rle_image2)
    print_image(image2)
    print("\t\tImage 3\n")
    image3 = uncompress_rle_image(rle_image3)
    print_image(image3)

def main():
    task0()
    print("\n--- Task 1: Average numbers ---")
    #task1()
    print("\n--- Task 2: Text to dictionary---")
    #task2()
    print("\n--- Task 3: Deleting from list---")
    #task3()
    print("\n--- Task 4: RLE decoding  ---")
    task4()

    input("Press enter to end lab 6.")

if __name__ == '__main__':
    main()
