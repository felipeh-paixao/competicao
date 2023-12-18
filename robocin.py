#RobôCin

linha_1 = input()
base = int(linha_1.split()[0])
altura = int(linha_1.split()[1])
n_casos = int(input())
posicao = []
var = 0

for x in range(n_casos):
    linha_2 = input()
    base_robo = int(linha_2.split()[0])
    altura_robo = int(linha_2.split()[1])
    direcao_robo = linha_2.split()[2]
    rota = input()

    for passo in rota:
        if passo == 'D':
            if direcao_robo == 'N':
                direcao_robo = 'L'
            elif direcao_robo == 'L':
                direcao_robo = 'S'
            elif direcao_robo == 'S':
                direcao_robo = 'O'
            else:
                direcao_robo = 'N'
        elif passo == 'E':
            if direcao_robo == 'N':
                direcao_robo = 'O'
            elif direcao_robo == 'O':
                direcao_robo = 'S'
            elif direcao_robo == 'S':
                direcao_robo = 'L'
            else:
                direcao_robo = 'N'
        else:
            if direcao_robo == 'N':
                if altura_robo + 1 > altura:
                    if posicao.count(str(base) + str(altura_robo) + direcao_robo + passo):
                        pass
                    else:
                        posicao.append(str(base) + str(altura_robo) + direcao_robo + passo)                        
                        var = 1
                        break                
            elif direcao_robo == 'S':
                if altura_robo - 1 < altura:
                    if posicao.count(str(base) + str(altura_robo) + direcao_robo + passo):
                        pass
                    else:
                        posicao.append(str(base) + str(altura_robo) + direcao_robo + passo)                        
                        var = 1
                        break
                else:
                    altura -= 1
            elif direcao_robo == 'O':
                if base_robo - 1 < base:
                    if posicao.count(str(base) + str(altura_robo) + direcao_robo + passo):
                        pass
                    else:
                        posicao.append(str(base) + str(altura_robo) + direcao_robo + passo)                        
                        var = 1
                        break 
            else:
                if base_robo + 1 > base:
                    if posicao.count(str(base) + str(altura_robo) + direcao_robo + passo):
                        pass
                    else:
                        posicao.append(str(base) + str(altura_robo) + direcao_robo + passo)                        
                        var = 1
                        break 
    
    if var:
        print(f'{base_robo} {altura} {direcao_robo} PERDIDO')
    else:
        print(f'{base_robo} {altura} {direcao_robo}')
