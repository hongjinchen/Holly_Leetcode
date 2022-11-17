s = "IX"
string_list = []
number_list = []
result = 0
for index in range(len(s)):
    string_list.append(s[index:index + 1])
for item in string_list:
    if item == "I":
        number_list.append(1)
    elif item == "V":
        number_list.append(5)
    elif item == "X":
        number_list.append(10)
    elif item == "L":
        number_list.append(50)
    elif item == "C":
        number_list.append(100)
    elif item == "D":
        number_list.append(500)
    elif item == "M":
        number_list.append(1000)
pre_number = 0
for item in number_list:
    if item < pre_number:
        result += item
        pre_number = item
    else:
        result -= pre_number*2
        pre_number = item
        result += item
print(result)
