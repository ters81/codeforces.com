s = input()

a=0
b=0

for i in s:
    if i>='a' and i<='z':
        a+=1
    else:
        b+=1
if a>=b:
    print(s.lower())
else:
    print(s.upper())
