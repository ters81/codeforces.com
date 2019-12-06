n = int(input())

x = list(map(int,input().split()))

for i in range(n):
    a = x.index(i+1)
    print(a+1, end=' ')
