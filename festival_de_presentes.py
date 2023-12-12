casos = int(input())
for x in range(casos):
    num_amigos = int(input())
    pessoas = input()
    pessoas = pessoas.split(' ')
    carteira = []
    for z in range(num_amigos):
        carteira.append(0)
    
    for i in range(num_amigos):
        linha = input()
        
