linha = input().split()
n = int(linha[0])
m = int(linha[1])
x = 0
y = 0
min_value = 0
max_value = 0
air = []
linha_1 = input().split()

for lin in linha_1:
    air.append(int(lin))


min_list = sorted(air) 
max_list = sorted(air)
while(x < n):
    max_value += max(max_list)
    max_list[max_list.index(max(max_list))] -= 1
    
    min_value += min_list[y]
    min_list[y] -= 1
    if min_list[y] <= 0:
        y += 1
    x += 1

print(f'{max_value} {min_value}')