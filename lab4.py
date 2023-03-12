import random
import time


def print_student_info():
    print("Name: Tamas Borbely")

def get_int_input(prompt, min_value, max_value):
    task1step1 = True

    while task1step1:
        int_input1  = int(input(prompt))

        if int_input1 >= min_value and int_input1 <= max_value:
            task1step1 = False
            return int_input1
        else:
            task1step1 = True

def task1():
    global get_int_input
    def get_int_input(prompt, min_value, max_value):
        task1step1 = True

        while task1step1:
            int_input1  = int(input(prompt))

            if int_input1 >= min_value and int_input1 <= max_value:
                task1step1 = False
                return int_input1
            else:
                task1step1 = True

    global get_yes
    def get_yes(prompt):
        step2 = True

        while step2:
            str_input1  = str(input(prompt)).upper()

            if str_input1 == "Y":
                step2 = False
                return True 
            elif str_input1 == "N":
                step2 = False
                return False 
            else:
                step2 
                


    randm = False
    def draw_owl(position, randomize):
        eye1 = '{o,o}'
        eye2 = '{-,o}'
        eye3 = '{o,-}'
        body = '/)_) '
        feet = ' " " '
        owl = ""
        owl += " "*position

        if randomize:
            random_eye = random.randint(1,3) 

            if random_eye == 1:
                print(owl + eye1)
            elif random_eye == 2:
                print(owl + eye2)
            elif random_eye == 3:
                print(owl + eye3)
        else:
            print(owl + eye1)

        print(owl + body) 
        print(owl + feet)
    
    N = get_int_input("How many times to move [2-20]? ", 2, 20)
    T = get_int_input("How long to delay [1-1000ms]? ", 1, 1000)
    randm = get_yes("Randomize [Y/N]? ")
    for i in range(N):
        draw_owl(i, randm)
        time.sleep(T / 1000)

def task2():
    def get_float_input(prompt, min_value, max_value):
        task2step1 = True
        while task2step1:
            float_input1  = float(input(prompt))

            if float_input1 >= min_value and float_input1 <= max_value:
                task2step1 = False
                return float_input1
            else:
                task2step1 

    def compute_return(amount, rate, years):
        amount_old = amount

        for i in range(years):
            amount_new = amount_old + amount_old * rate
            amount_old = amount_new

        return amount_new
    

    new_investment = True
    while new_investment:
        investmentamount = get_float_input("Input intial investment amount [1, 10000]? ", 1, 10000)
        return_rate = get_float_input("Annual return rate [0-1]? ", 0, 1)
        num_years = get_int_input("How many years [1-10]? ", 1, 10)
        result = compute_return(investmentamount, return_rate, num_years)

        if num_years > 1:
            print(f"Return in {num_years} years is: $ {result:10.2f}")
        else:
            print(f"Return in {num_years} year is: $ {result:10.2f}")
        new_investment = get_yes("Compute new investment [Y/N]? ")

def task3():
    global num_of_jumps
    num_of_jumps = 0 
    attempt = 4
    maxodd = 1
    for i in range(attempt):
        number_entered = get_int_input(f"{i+1}/5 Enter a number [1-100]: ", 1, 100)

        if number_entered % 2 != 0:
            if number_entered > maxodd:
                maxodd = number_entered

    print(f"Final max odd number: {maxodd}.")
    num_of_jumps = maxodd

def task4():
    input2  = str(input(f"Press enter to preform {num_of_jumps} jumping jacks"))
    for i in range(num_of_jumps):
        frame1 = f"  o   [  {i+1}]\n /|\  \n / \  "
        frame2 = f" \o/  [  {i+1}]\n  |   \n / \  "

        if i % 2 != 0:
            print(frame1)
        elif i % 2 == 0:
            print(frame2)

        time.sleep(0.3)

def main():
    print_student_info()

    print("\n---- Task 1: The Owl ----")
    task1()
    print("\n---- Task 2: Compound investment ---")
    task2()
    print("\n---- Task 3: Max odd number ----")
    task3()
    print("\n---- Task 4: Jumping Jacks ----")
    task4()
    input("Press enter to end lab 4.")

if __name__ == "__main__":
    main()
