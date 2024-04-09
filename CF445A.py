linha = input().split()
n = int(linha[0])
m = int(linha[1])
board = []

for i in range(n):
    board.append(input())

if n == 1 and m == 1:
    if board[0][0] == '.':
        print('B')
    else:
        print('-')
else:
    for i, line in enumerate(board):
        for j, house in enumerate(line):
            if house == '.':                
                if j == 0:
                    if i == 0 and j == 0: #P/ vertise superior esquerdo
                        if board[i][j + 1] == 'W' or board[i + 1][j] == 'W':
                            board[i] = 'B' + board[i][j + 1:]
                        else:
                            board[i] = 'W' + board[i][j + 1:]
                    elif i + 1 == n and j == 0: #P/ vertise inferior esquerdo
                        if board[i][j + 1] == 'W' or board[i - 1][j] == 'W':
                            board[i] = 'B' + board[i][j + 1:]
                        else:
                            board[i] = 'W' + board[i][j + 1:]
                    else:
                        if board[i][j + 1] == 'W' or board[i - 1][j] == 'W' or board[i + 1][j] == 'W':
                            board[i] = 'B' + board[i][j + 1:]
                        else:
                            board[i] = 'W' + board[i][j + 1:]

                if i == 0:
                    if i == 0 and j + 1 == m: #P/ vertise superior direito
                        if board[i][j - 1] == 'W' or board[i + 1][j] == 'W':
                            board[i] = board[i][:-1] + 'B'
                        else:
                            board[i] = board[i][:-1] + 'W'                           
                    elif i + 1 == n and j + 1 == m: #P/ vertise inferior esquerdo
                        if board[i][j - 1] == 'W' or board[i - 1][j] == 'W':
                            board[i] = board[i][:-1] + 'B'
                        else:
                            board[i] = board[i][:-1] + 'W'
                    else:
                        if board[i][j - 1] == 'W' or board[i + 1][j] == 'W' or board[i - 1][j]:
                            board[i] = board[i][:-1] + 'B'
                        else:
                            board[i] = board[i][:-1] + 'W'              
                
                
print(board)