
# dict={1:0,2:0,3:4}
# for item in dict:
#     print(item)
#     print(dict[item])
number=4
def FIBONACCI(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    return FIBONACCI(number-1)+FIBONACCI(number-2)
print(FIBONACCI(number))
