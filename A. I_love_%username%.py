n = int(input())

a = list(map(int,input().split()))

b = []
b.append(a[0])

x=0

for i in range(1,n):
    if a[i]>max(b) or a[i]<min(b):
        b.append(a[i])
        x+=1
    else:
        x+=0
print(x)
