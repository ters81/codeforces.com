n, k = map(int,input().split())

y = list(map(int, input().split()))

s = 0

for i in range(n):
    if y[i-1]<=(5-k):
        s+=1
    else:
        s+=0

print(s//3)
