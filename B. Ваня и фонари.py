n, l = map(int,input().split())
x = list(map(int,input().split()))

maximum=0

x.sort()

for i in range(n-1):
    if x[i+1]-x[i]>maximum:
        maximum=x[i+1]-x[i]

print(max(float(min(x)), float(l-max(x)), maximum/2))
