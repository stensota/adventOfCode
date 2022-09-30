

from tempfile import TemporaryDirectory


f = open("input.txt", "r")

#print(f.readlines())
string = f.readlines()
#print(f.readline())

open = ["(", "[", "{", "<"]
close = [")", "]", "}", ">"]

dict = {
    ")" : "(",
    "]" : "[",
    "}" : "{",
    ">" : "<"
}

illeagal_characters = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

total = 0

for lines in string:
    print(lines)
    temp_list = []
    for element in lines:
        if element in open:
            temp_list.append(element)
        elif element in close:
            if dict[element] == temp_list[len(temp_list)-1]:
                temp_list.pop()
            else: 
                print("ILLEGAL CHARACTER")
                print(element)
                total = total + illeagal_characters[element]
                break

print(total)