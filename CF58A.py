s = input()
palavra = 'hello'
teste = 0

if len(s) <= 5:
    print('NO')
else:   
    for i in range(len(s)):
        for j in range(i,len(s),1):
            if palavra[teste] == s[j]:
                teste += 1
            
        if teste == 5:
            print('YES')
            break
        else:
            teste = 0
    
    if i == len(s):
        print('NO')