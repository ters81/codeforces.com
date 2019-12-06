n = int(input())

x=0

for i in range(n):
    p, q = map(int, input().split())
    if (q-p)>=2:
        x+=1

print(x)
