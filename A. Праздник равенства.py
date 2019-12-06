n = int(input())

a = list(map(int,input().split()))

s = 0

for i in range(n):
    if a[i]<max(a):
        s=s+max(a)-a[i]
    else:
        s+=0

print(s)
