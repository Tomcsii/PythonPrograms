import random

def print_student_info():
    print("Name: Tamas Borbely")

# class for task 2
class virus:
    DNA = ""
    def __init__(self, DNAinput=""):

        AGCT = set(DNAinput)
        for letter in AGCT:
            if letter == 'A' or letter == 'G' or letter == 'C' or letter == 'T':
                onlyAGCT = True
            else:
                onlyAGCT = False

        if len(DNAinput) == 50 and onlyAGCT:
            self.DNA = DNAinput 
        else:
            rand_dna = ""
            letters = ["A", "C", "G", "T"]
            for i in range(50):
                new_letter = random.randint(1, 4)
                rand_dna += letters[new_letter - 1]
            self.DNA = rand_dna

    def getDNA(self):
        return self.DNA
    
    def replicate(self):

        random_num = random.randint(1,100)
        if random_num > 94:
            random_num2 = random.randint(1,49)
            mutatedDNA = list(self.DNA)
            letters = ["A", "C", "G", "T"]
            new_letter = random.randint(1, 4)
            mutatedDNA[random_num2 - 1] = letters[new_letter - 1]
            new_mut_dna = ""
            for letter in mutatedDNA:
                new_mut_dna += letter
            new_virus = virus(new_mut_dna)
        else:
            new_virus = virus(self.DNA)
        return new_virus

def find_mutation(virus1, virus2):
    v1 = virus1.getDNA()
    v2 = virus2.getDNA()
    v1 = list(v1)
    v2 = list(v2)
    indicator = ""
    for i in range(50):
        if v1[i] == v2[i]:
            indicator += " "
        else:
            indicator += "^"
    return indicator

# class for task 1
class lotto_ticket:
    ticket_counter = 1

    def __init__(self):
        self.ticket_id = lotto_ticket.ticket_counter        
        lotto_ticket.ticket_counter = lotto_ticket.ticket_counter + 1

        random_set = {}
        random_set = set()

        while len(random_set) < 5:
            random_num = random.randint(1,20)

            if random_num in random_set:
                None
            else:
                random_set.add(random_num)

        self.numbers =  random_set

    def print_ticket(self):
        print(f"Ticket #[ {self.ticket_id:2}]", end="")
        for item in self.numbers:
            print(f"  {item:2}  ", end="")
        print()
            
    def print_and_return_win(self, lotto_numbers):
        combined_set = lotto_numbers.intersection(self.numbers)

        print(f"Ticket #[ {self.ticket_id:2}]", end="")
        for item in self.numbers:
            if item in combined_set:
                print(f" *{item:02}* ", end="")
            else:
                print(f"  {item:02}  ", end="")
            

        print(f"\t[{len(combined_set)} matches, $", end="")
        if len(combined_set) == 0 or len(combined_set) == 1 or len(combined_set) == 2:
            print("0]")
            return 0
        elif len(combined_set) == 3:
            print("2]")
            return 2
        elif len(combined_set) == 4:
            print("20]")
            return 20
        elif len(combined_set) == 5:
            print("100]")
            return 100

def lotto_draw():
    draw = {}
    draw = set()

    while len(draw) < 5:
        random_num = random.randint(1,20)

        if random_num in draw:
            None
        else:
            draw.add(random_num)
    
    return draw
  
def task0():
    print_student_info()

def task1():
    amount = 100
    while amount >= 2:
        ticket_amount = -1
        while ticket_amount*2 > amount or ticket_amount < 0: 
            print(f"You have ${amount}")
            ticket_amount = int(input("How many lotto tickets do you want [$2 each]? "))
        if ticket_amount == 0:
            
            break
        else:
            amount -= ticket_amount*2
        new_list = []
        for i in range(ticket_amount):
            new_ticket = lotto_ticket()
            new_ticket.print_ticket()
            new_list.append(new_ticket)
        cpu_draw = lotto_draw()
        print(f"--LOTTO DRAW--")
        for num in cpu_draw:
            print(f"{num} ", end="")
        print()
        input("---Press enter to check your winnings---")
        for item in new_list:
            won = item.print_and_return_win(cpu_draw)
            amount += won 
    print(f"You have ${amount}")

def task2():
    YN = "Y"
    while YN == "Y":
        name = input("Name of virus: ")
        my_virus = virus()
        original_virus = my_virus
        print(f"Original dna sequence: {my_virus.getDNA()}")
        N = int(input("How many times to replicate? "))
        for i in range(N):
            my_virus = my_virus.replicate()
            print(f"Replica [{ i:2}] DNA sequence: {my_virus.getDNA()}")
        print(f"Comparing latest {name} virus to the original {name}.")
        mutation_location = find_mutation(original_virus, my_virus)
        mutation_num = mutation_location.count('^')
        if mutation_num == 0:
            print("No mutations detected")
        elif mutation_num <= 5:
            print(f"{original_virus.getDNA()}\n{my_virus.getDNA()}\n{mutation_location}")
            print(f"{mutation_num} mutations -- virus is the same.")
        elif mutation_num > 5:
            print(f"{original_virus.getDNA()}\n{my_virus.getDNA()}\n{mutation_location}")
            print(f"{mutation_num} mutations -- a *new* virus has been created")
        YN = input("Try again? ").upper()

def main():
    task0()
    print("\n--- Task 1: Lotto LESS Revisited ---")
    task1()
    print("\n--- Task 2: Virus mutator ---")
    task2()

if __name__ == "__main__":
      main()