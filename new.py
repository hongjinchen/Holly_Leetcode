a=[[".1.2.3.256"],["1.2.3.1"]]


number_list = [0] * 4
index = 0
Isbreak=False
for item in a:
    if item[0][0]=="." or item[0][-1]==".":
        print("invalid")
        Isbreak=True
        break
    if Isbreak:
        break
    item = list(item[0])
    numbers=""
    for number in item:
        if number != ".":
            numbers+=number
        else:
            number_list[index] += int(numbers)
            index += 1
            numbers=""
    if numbers!="":
        number_list[index] += int(numbers)

    index = 0
answer=""
for number in number_list:
    if number>=255:
        number=0
    answer+=str(number)+"."

answer=answer[:-1]
print(answer)