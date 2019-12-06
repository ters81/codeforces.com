n, k = map(int,input().split())

a = list(map(int,input().split()))

s = 0

a.insert(0,0)

for i in range(n+1):
    if a[i]>=a[k] and a[i]>0:
        s+=1
    else:
        s+=0
        
print(s)
