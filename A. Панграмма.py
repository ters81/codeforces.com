n = int(input())
a = input()

a = a.lower()
b = 'abcdefghijklmnopqrstuvwxyz'
s = 0

if len(a)<26:
    print('NO')
else:
    for i in b:
        if i in a:
            s+=1
        else:
            s+=0
    if s==26:
        print('YES')
    else:
        print('NO')
