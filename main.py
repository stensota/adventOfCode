

def illeagal_line(line):
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
                return True


f = open("input.txt", "r")

string = f.readlines()

incomplete = []
for lines in string:
    if illeagal_line(lines):
        continue
    else:
        incomplete.append(lines)

print (incomplete)
