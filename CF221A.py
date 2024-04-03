n = int(input())
series = [n]

for i in range(1, n, 1):
    series.append(i)

for number in series:
    print(number, end=' ')