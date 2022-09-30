

from tempfile import TemporaryDirectory


f = open("input.txt", "r")

#print(f.readlines())
string = f.readlines()
#print(f.readline())

open = ["(", "[", "{", "<"]
close = [")", "]", "}", ">"]

temp_list = []

print(string[1])

for element in string[1]:
    print(element)
    if element in open:
        temp_list.append(element)

print(temp_list)