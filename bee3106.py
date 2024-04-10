n = int(input())
x = n
linha = input().split()
classes = []
alunos = 0
for lin in linha:
    alunos += int(lin) - int(lin) % 3

print(alunos)