board=[['O', 'K', 'B'], ['O', 'K', 'B'], ['O', 'K', 'O']]
# 找出K还是B赢了

is_winner=False
for index in range(3):
    # 横向比较
    if board[index][0]==board[index][1] and board[index][1]==board[index][2]:
        if board[index][0]=='K':
            print("KiKi wins!")
            is_winner=True
        elif board[index][0]=='B':
            print("BoBo wins!")
            is_winner=True
            
    # 竖向比较
    if board[0][index]==board[1][index] and board[1][index]==board[2][index]:
        if board[0][index]=='K':
            print("KiKi wins!")
            is_winner=True
        elif board[0][index]=='B':
            print("BoBo wins!")
            is_winner=True


    # 斜方向比较
if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        if board[0][0]=='K':
            print("KiKi wins!")
            is_winner=True
        elif board[0][0]=='B':
            print("BoBo wins!")
            is_winner=True
            
if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        if board[0][2]=='K':
            print("KiKi wins!")
            is_winner=True
        elif  board[0][2]=='B':
            print("BoBo wins!")  
            is_winner=True
    
if is_winner==False:
    print("No winner!")