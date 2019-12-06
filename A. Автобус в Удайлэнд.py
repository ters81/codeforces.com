n = int(input())

b=[]
c=''

for i in range(n):
    a = input()
    b.append(a)
    c=c+' '+a
    c=c.strip()

if 'OO|' in c:
    print('YES')
    for i in range(n):
        if 'OO' in str(b[i]):
            b[i]=b[i].replace('OO|', '++|')
            break
    for i in range(n):
        print(b[i])
        
        
elif '|OO' in c:
    print('YES')
    for i in range(n):
        if '|OO' in str(b[i]):
            b[i]=b[i].replace('|OO', '|++')
            break
          
    for i in range(n):
        print(b[i])

else:
    print('NO')
