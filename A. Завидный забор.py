t = int(input())

r=[]

for i in range(t):
    
    a = int(input())
    n = 360/(180-a)
        
    if a<60 or a>180:
        r.append('NO')
    elif a>=60 and a <=180 and n==int(n):
        r.append('YES')
    else:
        r.append('NO')
        
for i in range(t):
    print(r[i])
