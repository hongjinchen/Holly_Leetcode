board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]
# 数字 1-9 在每一行只能出现一次
for row in board:
    List = []
    for item in row:
        if item != ".":
            if int(item) not in List:
                List.append(int(item))
            else:
                print(False, 1)
# 数字 1-9 在每一列只能出现一次。
for i in range(9):
    List = []
    for row in board:
        if row[i] != ".":
            if int(row[i]) not in List:
                List.append(int(row[i]))
            else:
                print(False, 2)
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
number_list = [0, 3, 6]
for start_x in number_list:
    for start_y in number_list:
        List = []
        for number in range(start_y, start_y + 3):
            for x in range(start_x, start_x + 3):
                if board[number][x] != ".":
                    if int(board[number][x]) not in List:
                        List.append(int(board[number][x]))
                    else:
                        print(board[number][x])
                        print(List)
                        print(False, 3)
print(True)
