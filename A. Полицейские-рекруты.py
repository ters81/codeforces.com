n = int(input())

a = list(map(int,input().split()))

x=0
y=0

for i in range(n):
    x=x+a[i]
    if x>=0:
        x=x+0
        y=y+0
    else:
        x=0
        y+=1

print(y)
