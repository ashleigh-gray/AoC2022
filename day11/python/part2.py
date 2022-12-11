testing = False

class monkey:
    def __init__(self):
        self.number = 0
        self.items = []
        self.operation = ''
        self.test = ''
        self.iftrue = 0
        self.iffalse = 0
        self.inspected = 0
        
    def add_number(self, number):
        self.number = number
        
    def add_items(self, items):
        self.items = items
        
    def add_operation(self, operation):
        self.operation = operation
        
    def add_test(self, test):
        self.test = test
        
    def add_iftrue(self, iftrue):
        self.iftrue = iftrue
        
    def add_iffalse(self, iffalse):
        self.iffalse = iffalse
        
    def perform_operation(self, item):
        if self.operation[0] == "+":
            item = item + int(self.operation[1:])
        elif self.operation[0] == "-":
            item = item - int(self.operation[1:])
        elif self.operation[0] == "*":
            item = item * int(self.operation[1:])
        elif self.operation[0] == "/":
            item = item / int(self.operation[1:])
        elif self.operation == "sqrt":
            item = item * item
        elif self.operation == "0":
            item = 0
        elif self.operation == "1":
            item = 1
        return item
            
    def perform_test(self, item):
        if item%self.test == 0:
            return True
        else:
            return False
        
    def print_monkey(self):
        print("--------------------------")
        print("Monkey number:", self.number)
        print("Monkey items:", self.items)
        print("Operation:", self.operation)
        print("Test:", self.test)
        print("If true, item goes to monkey:", self.iftrue)
        print("If false, item goes to monkey:", self.iffalse)

    def print_monkey_items(self):
        print("--------------------------")
        print("Monkey:", self.number, self.items)
        print("Inspected", self.inspected, "items")
        
if testing == True:
    filename = "../sample_input.txt"
elif testing == False:
    filename = "../input.txt"
    
input = open(filename, 'r')
lines = input.read().splitlines()

monkeys = []
rounds = 10000
lcm = 1

for line in lines:
    if "Monkey" in line:
        current_monkey = monkey()
        number = int(line.split(' ')[1][0])
        current_monkey.add_number(number)
    elif "Starting items:" in line:
        items = [int(x) for x in line.split(': ')[1:][0].split(', ')]
        current_monkey.add_items(items)
    elif "Operation:" in line:
        full_rule = line.split(' ')[1:]
        change = line.split(' ')[3:]
        left = change[2]
        operand = change[3]
        right = change[4]
        if left != "old":
            print("found an operation rule breaker")
            continue
        if right == "old":
            if operand == "+":
                operation = "*2"
            elif operand == "-":
                operation = "0"
            elif operand == "*":
                operation = "sqrt"
            elif operand == "/":
                operation = "1"
        else:
            operation = operand + right
        current_monkey.add_operation(operation)
    elif "Test:" in line:
        full_test = line.split(' ')[3:]
        if full_test[0] != "divisible":
            print("found a test rulebreaker")
        else:
            test = int(full_test[2])
            lcm = lcm*test
        current_monkey.add_test(test)
    elif "If true:" in line:
        next_monkey = int(line.split(' ')[9])
        current_monkey.add_iftrue(next_monkey)
    elif "If false:" in line:
        next_monkey = int(line.split(' ')[9])
        current_monkey.add_iffalse(next_monkey)
        monkeys.append(current_monkey)

for r in range(rounds):
    for m in monkeys:
        og_list = list(m.items)
        for i in og_list:
            m.items.remove(i)
            i = m.perform_operation(i)%lcm
            m.inspected += 1
            if m.perform_test(i):
                monkeys[m.iftrue].items.append(i)
            else:
                monkeys[m.iffalse].items.append(i)

inspected = []
for m in monkeys:
    inspected.append(m.inspected)
    m.print_monkey_items()

highest_two = sorted(inspected, reverse=True)[0:2]

print("--------------------------")
print("Monkey business:", highest_two[0]*highest_two[1])