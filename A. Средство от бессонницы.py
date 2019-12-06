k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())


r=list(range(1,d+1))


for i in range(d):
    if r[i]%k==0:
        x=r[i]
        r.remove(x)
        r.insert(i,'0')
    elif r[i]%l==0:
        x=r[i]
        r.remove(x)
        r.insert(i,'0')
    elif r[i]%m==0:
        x=r[i]
        r.remove(x)
        r.insert(i,'0')
    elif r[i]%n==0:
        x=r[i]
        r.remove(x)
        r.insert(i,'0')
x=r.count('0')
print(x)
