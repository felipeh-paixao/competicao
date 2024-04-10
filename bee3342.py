n = int(input())

if n % 2 == 0:
    print(f'{(n * n) // 2} casas brancas e {(n * n) // 2} casas pretas')
else:
    print(f'{((n * n) // 2) + 1} casas brancas e {((n * n)  - 1) // 2} casas pretas')