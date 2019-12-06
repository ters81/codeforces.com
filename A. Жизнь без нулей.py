a = int(input())
b = int(input())

c=a+b

a1=''

while a>0:
    lasta = a % 10
    if lasta!=0:
        a1=a1+str(lasta)
        a = a // 10
    else:
        a = a // 10
a1=a1[::-1]


b1=''

while b>0:
    lastb = b % 10
    if lastb!=0:
        b1=b1+str(lastb)
        b = b // 10
    else:
        b = b // 10
b1=b1[::-1]


c1=''

while c>0:
    lastc = c % 10
    if lastc!=0:
        c1=c1+str(lastc)
        c = c // 10
    else:
        c = c // 10
c1=c1[::-1]


if int(a1)+int(b1)==int(c1):
    print('YES')
else:
    print('NO')
