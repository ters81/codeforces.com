n = int(input())

p = list(map(int, input().split()))

x = 0

for i in range(n):
    x = float(x+(p[i-1]/100))

print(float((x/n)*100))
