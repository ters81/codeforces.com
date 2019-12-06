x = input()
y = input()

a='qwertyuiop'
b='asdfghjkl;'
c='zxcvbnm,./'

d=''

for i in y:
    if x=='R' and i in a:
        i=a.index(i)-1
        d=d+a[i]
    elif x=='R' and i in b:
        i=b.index(i)-1
        d=d+b[i]
    elif x=='R' and i in c:
        i=c.index(i)-1
        d=d+c[i]
    elif x=='L' and i in a:
        i=a.index(i)+1
        d=d+a[i]
    elif x=='L' and i in b:
        i=b.index(i)+1
        d=d+b[i]
    elif x=='L' and i in c:
        i=c.index(i)+1
        d=d+c[i]
print(d)
