def print_student_info():
    print("Name: Tamas Borbely")

def task0():
    print_student_info()

def is_sorted(a_list):
    if len(a_list) > 0:
        for i in range(len(a_list)):
            if i+1 != len(a_list):
                if a_list[i] <= a_list[i+1]:
                    continue
                else:
                    return False
            else:
                continue
        return True       
    else: 
        return True



def task1():
    x1 = [1, 4, 5, 9, 0, 8, 10]
    x2 = [1, 2, 4, 5, 6, 7, 9]
    x3 = []
    # Write function is_sorted() outside this function
    # apply the function on each list and print the results
    print(is_sorted(x1))
    print(is_sorted(x2))
    print(is_sorted(x3))

def merge_dict(dict1, dict2):
    for key in dict2:
        if key in dict1:
            continue
        else:
            dict1.update({key:dict2[key]})

def task2():
    dict1 = {8:"Exercise", 9:"Breakfast", 12:"Lunch", 3:"Study", 6:"Netflix"}
    dict2 = {8:"Sleep", 10:"Lab", 12:"Class", 4:"Call Mom"}
    # Write function merge_dict() outside this function
    # print dict1
    print(f"dict1\n{dict1}")
    # print dict2
    print(f"dict2\n{dict2}")
    # call merge_dict(dict1, dict2)  <- which will modified dict1
    merge_dict(dict1, dict2)
    # print dict1 again (after it is modified)
    print(f"dict2 merged into dic1\n{dict1}")

def invert_dict(a_dict):
    b_dict = {}
    for key in a_dict:
        b_dict.update({a_dict[key]:key})
    return b_dict

def task3():
    a_dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
    # write function invert_dict() outside this function
    # print a_dict
    print(a_dict)
    # call invert_dict(a_dict)
    new_dict = invert_dict(a_dict)
    # print new dict
    print(new_dict)

def list_to_dict(a_list):
    empty_dict = {}
    for i in range(len(a_list)):
        empty_dict.update({a_list.index(a_list[i]):a_list[i]})
    return empty_dict

def task4():
    my_list = [1, "hello", 9.99, ["EECS", "1015"], {1:"1", 2:"2"}]
    # write function list_to_dict() outside this function
    # print list
    print(my_list)
    # call list_to_dict(my_list)
    new_dict = list_to_dict(my_list)
    # print new dictionary
    print(new_dict)

def str_list_to_num_list(a_list):
    for i in range(len(a_list)):
        a_list.insert(i, int(a_list[i]))
        a_list.remove(a_list[i+1])

def task5():
    x = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # write fucntion str_list_to_num_list()
    # print list x
    print(x)
    # call function str_list_to_num_list(x)
    str_list_to_num_list(x)
    # print list x again (it should be updated)
    print(x)
    
def merge_lists(list1, list2):

    new_list = [] 
    len1 = len(list1) 
    len2 = len(list2) 
    index1 = 0 
    index2 = 0

    assert is_sorted(list1), "List 1 is not sorted!" 
    assert is_sorted(list2), "List 2 is not sorted!"

    while index1 < len1 and index2 < len2: 
        if list1[index1] <= list2[index2]: 
            new_list.append(list1[index1]) 
            index1 += 1 
        else: 
            new_list.append(list2[index2]) 
            index2 += 1 
    if index1 < len1: 
        new_list.extend(list1[index1:]) 
    if index2 < len2: 
        new_list.extend(list2[index2:]) 
    return new_list

def task6():
    YN = "Y"
    while YN == "Y":
        list_input1 = list(input("Input 1st list of sorted numbers [x1, x2, ...]: ").split(" "))
        str_list_to_num_list(list_input1)
        list_input2 = list(input("Input 2st list of sorted numbers [y1, y2, ...]: ").split(" "))
        str_list_to_num_list(list_input2)
        merged_list = merge_lists(list_input1, list_input2)
        print(merged_list)
        YN = input("Merge again? ").upper()

def main():
    print("\n---- Task 1: Check if list is sorted ----")
    task1()
    print("\n---- Task 2: Merge dictionaries ----")
    task2()
    print("\n---- Task 3: Invert dictionaries ----")
    task3()
    print("\n---- Task 4: List to dictionary ----")
    task4()
    print("\n---- Task 5: String list to num list ----")
    task5()
    print("\n---- Task 6: Merge list with assert ----")
    task6()

if __name__ == "__main__":
    main()