n = int(input())
stack = []
for i in range(n):
    temp = input().split()
    if len(temp) == 1:
        if len(stack):            
            if temp[0] == 'MIN':
                print(min(stack))
            else:
                stack.pop()
        else:
            print('EMPTY')
    else:
        stack.append(int(temp[1]))