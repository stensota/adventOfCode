

from xmlrpc.client import Boolean
import statistics


def check_line(line, illegal : Boolean = False, complete : Boolean = False):
    open = ["(", "[", "{", "<"]
    close = [")", "]", "}", ">"]

    dict = {
        ")" : "(",
        "]" : "[",
        "}" : "{",
        ">" : "<"
    }
    
    temp_list = []
    for element in lines:
        if element in open:
            temp_list.append(element)
        elif element in close:
            if dict[element] == temp_list[len(temp_list)-1]:
                temp_list.pop()
            else:
                if illegal:
                    return True

    if complete:
        inv_map = {v: k for k, v in dict.items()}
        completed = []
        for entry in reversed(temp_list):
            completed.append(inv_map[entry])
        return completed



f = open("input.txt", "r")

string = f.readlines()

illegal_characters = {
     ")" : 1,
     "]" : 2,
     "}" : 3,
     ">" : 4
 }

incomplete = []
for lines in string:
    if check_line(lines, illegal=True):
        continue
    else:
        incomplete.append(lines)

print(incomplete)

totals = []
for lines in incomplete:
    total = 0
    for char in check_line(lines, complete=True):
        total = total * 5 + illegal_characters[char]
    
    totals.append(total)

print(statistics.median(totals))
