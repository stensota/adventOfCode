

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

temp_list = []

print(string[1])
for element in string[1]:
    if element in open:
        temp_list.append(element)
    elif element in close:
        if dict[element] == temp_list[len(temp_list)-1]:
            temp_list.pop()
        else: 
            print("ILLEGAL CHARACTER")
            print(element)
            break
        
