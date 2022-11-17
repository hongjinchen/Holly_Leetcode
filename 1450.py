startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4
if len(startTime) < 1:
    print(0)
studentTime = []
result = 0
for index in range(len(startTime)):
    studentTime.append([startTime[index], endTime[index]])

for item in studentTime:
    if queryTime >= item[0] and queryTime <= item[1]:
        result += 1

print(result)
