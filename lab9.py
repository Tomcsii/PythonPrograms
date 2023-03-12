import random

def student_info():
    print("Name: Tamas Borbely")

def task0():
    student_info()

def task1():
    YN = "Y"
    while YN == "Y":
        user_input = list(input(f"Type in a long sentance: ").split(" "))  
        substring = input(f"Remove words conataining: ")
        words_remove = ""
        words_stay = ""

        for word in user_input:
            if word.count(substring) > 0:
                if words_remove == "":
                    words_remove += word
                else:
                    words_remove += " " + word
            else:
                if words_stay == "":
                    words_stay += word
                else:
                    words_stay += " " + word

        print(f"Wtih substring: \'{words_remove}\'")
        print(f"Without substring: \'{words_stay}\'")
        YN = input("Try again? [Y/N] ").upper()

# write randomlist and reshape for task2 below
def randommlist(N):
    empty_list = []
    for i in range(N):
        empty_list.append(random.randint(0,9))
    return empty_list

def reshape(a_list, num_rows, num_cols):
    empty_list = []
    
    for i in range(num_rows):
        new_list = []
        empty_list.append(new_list)
    
    count = 0
    while count != len(a_list):
        for list in empty_list:
            while len(list) < num_cols:
                list.append(a_list[count])
                count += 1

    return empty_list

def task2():
    YN = "Y"

    while YN == "Y":
        list_len = int(input(f"List length: "))
        random_list = randommlist(list_len)
        print(random_list)
        row = int(input(f"Rows: "))
        col = int(input(f"Cols: "))
        if row*col != list_len:
            print(f"Error: {row}*{col} != {list_len}")
        else:
            new_list = reshape(random_list, row, col)
            print(f"Reshaped list {new_list}")
        YN = input("Try again? [Y/N] ").upper()

# write function find_duplicates() for task 3 below

def find_duplicate(a_dict):
    empty_dict = {}
    empty_dict = a_dict
    new_dict = {}
    for key in empty_dict:
        random_set = {}
        random_set = set()
        for keys in a_dict:
            if empty_dict[key] == a_dict[keys]:
                random_set.add(keys)
                new_list = list(random_set)
                if len(new_list) > 1:
                    new_dict.update({empty_dict[key]:new_list})

    return new_dict


def task3():
    YN = "Y"

    while YN == "Y":
        user_input = "1"
        count = 0
        user_dict = {}
        while user_input != "":
            count += 1
            user_input = input(f"[Input {count:2}] Word: ")
            user_dict.update({count:user_input})
        dup_dict = find_duplicate(user_dict)
        print(f"{dup_dict}")
        YN = input("Try again? ").upper()

# write class rangeChecker for task4 below

class rangeChecker:
    range_counter = 1

    def __init__(self, name, min, max):
        assert min < max, f"Max ({max:.2}) must be greater than min ({min:.2})"
        self.id = rangeChecker.range_counter
        rangeChecker.range_counter += 1 
        self.name = name
        self.max_value = max
        self.min_value = min
    
    def within_range(self, number) -> bool:
        if self.min_value < number < self.max_value:
            return True
        else:
            return False
    
    def outside_range(self, number) -> bool:
        if self.min_value > number or number > self.max_value:
            return True
        else:
            return False
    
    def print(self):
        print(f"rangeChecker [{self.id:2}] \'{self.name:10}\' - {self.min_value:8.2f} <= num <= {self.max_value:8.2f}")


def task4():
    YN = "Y"

    while YN == "Y":
        list_obj = []
        for i in range(3):
            user_objects = list(input(f"Range {i} Name, Min, Max: ").replace(" ", "").split(","))
            name = str(user_objects[0])
            min = float(user_objects[1])
            max = float(user_objects[2])
            list_obj.append(rangeChecker(name, min, max))
        num_list = list(input("Input list of numbers x1, x2,..,xn: ").replace(" ", "").split(","))

        for x in range(len(list_obj)):
            list_obj[x].print()
            for y in range(len(num_list)):
                num_list[y] = float(num_list[y])
                print(f"Inside range [{num_list[y]:8.2f}]: {list_obj[x].within_range(num_list[y])}")
                
        for x in range(len(list_obj)):
            list_obj[x].print()
            for y in range(len(num_list)):
                num_list[y] = float(num_list[y])
                print(f"Inside range [{num_list[y]:8.2f}]: {list_obj[x].outside_range(num_list[y])}")
        
        YN = input("Try again? ").upper()
                
            


def main():
    task0()
    print("--- Task 1 ---")
    task1()
    print("\n--- Task 2 ---")
    task2()
    print("\n--- Task 3 ---")
    task3()
    print("\n--- Task 4 ---")
    task4()

if __name__ == "__main__":
    main()