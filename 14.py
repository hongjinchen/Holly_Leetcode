strs = ["dog","racecar","car"]

def compareTwoString(string1, string2):
    stringLength = min(len(string1), len(string2))
    index = 0
    while index < stringLength and string1[index] == string2[index]:
        index += 1
    return string1[:index]
if not strs:
    print("")

result = strs[0]
index = len(strs[0])
for index in range(len(strs)):
    result = compareTwoString(result, strs[index])
    if not result:
        print("")
        break
print(result)



