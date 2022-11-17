points = [[1, 3], [3, 3], [5, 3], [2, 2]]
queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
answer = []

for curve in queries:
    number=0
    for point in points:
        if ((curve[0] - point[0])**2+(curve[1] - point[1])**2)**0.5 <= curve[2]:
            number=number+1
    answer.append(number)
print(answer)        
