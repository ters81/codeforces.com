n = int(input())
a = list(map(int,input().split()))

a.sort(reverse=True)
s=0
x=0

for i in range(n):
    if s<=sum(a[i::]):
             s=s+a[i]
             x+=1
print(x)
