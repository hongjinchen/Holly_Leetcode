num = 9
dictionary={1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

answer=""
if num==4:
    print("IV")
while num!=0:
    for key in dictionary:
        if num//key!=0:
            number=num//key
            answer+=number*dictionary[key]
            num=num-key*number
print(answer)