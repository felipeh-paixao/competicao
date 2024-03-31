try:       
    while True: 
        n = int(input())

        if n % 2:
            pass               

        for i in range(1,n + 1, 2):
            space = (n - i) // 2 
            print(' ' * space + '*' * i)

        for i in range(1, 4, 2):
            space = (n - i) // 2 
            print(' ' * space + '*' * i)        
        
        print()
except EOFError:
    pass