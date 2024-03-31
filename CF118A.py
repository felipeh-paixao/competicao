s = input()
s = s.lower()
new_s = ''
for letra in s:  
    if 'aoyeui'.count(letra) == 0:
        new_s =  new_s + '.' +letra

print(new_s)
'''s = '.' + new_s[0]

for i in range(1, len(new_s), 1):
    s = s + '.' + new_s[i]

print(s)'''