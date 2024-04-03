s = input()
s = s.lower()
new_s = ''
for letra in s:  
    if 'aoyeui'.count(letra) == 0:
        new_s =  new_s + '.' +letra

print(new_s)
