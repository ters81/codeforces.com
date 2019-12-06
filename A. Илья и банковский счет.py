n = int(input())

x = str(n)
a = len(x)

b = x[0:a-1]
c = x[0:a-2]+x[a-1:]

if n>=0:
    print(n)

elif -100<n<0 and int(c)==0:
    print('0')
   
elif b<c:
    print(b)
    
else:
    print(c)
