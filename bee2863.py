try:
    while(True):
        x = input()
        laps = []
        for i in range(int(x)):
            laps.append(float(input()))

        laps.sort()

        print(laps[0])
except EOFError:
    pass
