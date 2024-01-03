grid = [[1, 1, 1],[1, 1, 1],[1, 1, 1]]
press_boton = []

for i in range(3):
    press_boton.append(input())
    press_boton[i] = press_boton[i].split()


for i in range(3):
    for j in range(3):
        if int(press_boton[i][j]) % 2 == 1:
            if i == 0:
                if j == 0:
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                    
                    if grid[i + 1][j] == 0:
                        grid[i + 1][j] = 1
                    else:
                        grid[i + 1][j] = 0
                    
                    if grid[i][j + 1] == 0:
                        grid[i][j + 1] = 1
                    else:
                        grid[i][j + 1] = 0
                elif j == 1:
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                    
                    if grid[i + 1][j] == 0:
                        grid[i + 1][j] = 1
                    else:
                        grid[i + 1][j] = 0
                    
                    if grid[i][j + 1] == 0:
                        grid[i][j + 1] = 1
                    else:
                        grid[i][j + 1] = 0
                    
                    if grid[i][j - 1] == 0:
                        grid[i][j - 1] = 1
                    else:
                        grid[i][j - 1] = 0
                else:
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                    
                    if grid[i + 1][j] == 0:
                        grid[i + 1][j] = 1
                    else:
                        grid[i + 1][j] = 0
                    
                    if grid[i][j - 1] == 0:
                        grid[i][j - 1] = 1
                    else:
                        grid[i][j - 1] = 0
            
            elif i == 2:
                if j == 0:
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                    
                    if grid[i - 1][j] == 0:
                        grid[i - 1][j] = 1
                    else:
                        grid[i - 1][j] = 0
                    
                    if grid[i][j + 1] == 0:
                        grid[i][j + 1] = 1
                    else:
                        grid[i][j + 1] = 0
                elif j == 1:
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                    
                    if grid[i - 1][j] == 0:
                        grid[i - 1][j] = 1
                    else:
                        grid[i - 1][j] = 0
                    
                    if grid[i][j + 1] == 0:
                        grid[i][j + 1] = 1
                    else:
                        grid[i][j + 1] = 0
                    
                    if grid[i][j - 1] == 0:
                        grid[i][j - 1] = 1
                    else:
                        grid[i][j - 1] = 0
                else:
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                    
                    if grid[i - 1][j] == 0:
                        grid[i - 1][j] = 1
                    else:
                        grid[i - 1][j] = 0
                    
                    if grid[i][j - 1] == 0:
                        grid[i][j - 1] = 1
                    else:
                        grid[i][j - 1] = 0

            else:
                if j == 0:
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                    
                    if grid[i - 1][j] == 0:
                        grid[i - 1][j] = 1
                    else:
                        grid[i - 1][j] = 0
                    
                    if grid[i][j + 1] == 0:
                        grid[i][j + 1] = 1
                    else:
                        grid[i][j + 1] = 0
                    
                    if grid[i + 1][j] == 0:
                        grid[i + 1][j] = 1
                    else:
                        grid[i + 1][j] = 0
                elif j == 1:
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                    
                    if grid[i - 1][j] == 0:
                        grid[i - 1][j] = 1
                    else:
                        grid[i - 1][j] = 0
                    
                    if grid[i][j + 1] == 0:
                        grid[i][j + 1] = 1
                    else:
                        grid[i][j + 1] = 0
                    
                    if grid[i][j - 1] == 0:
                        grid[i][j - 1] = 1
                    else:
                        grid[i][j - 1] = 0
                    
                    if grid[i + 1][j] == 0:
                        grid[i + 1][j] = 1
                    else:
                        grid[i + 1][j] = 0
                else:
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                    
                    if grid[i - 1][j] == 0:
                        grid[i - 1][j] = 1
                    else:
                        grid[i - 1][j] = 0
                    
                    if grid[i][j - 1] == 0:
                        grid[i][j - 1] = 1
                    else:
                        grid[i][j - 1] = 0
                    
                    if grid[i + 1][j] == 0:
                        grid[i + 1][j] = 1
                    else:
                        grid[i + 1][j] = 0

for i in range(3):
    for j in range(3):
        if j < 2:
            print(grid[i][j], end='')
        else:
            print(str(grid[i][j]), end='')
    
    if i < 2:
        print()

