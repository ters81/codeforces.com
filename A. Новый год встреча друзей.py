x = list(map(int, input().split()))
x.sort()

a = x[0]
b = x[1]
c = x[2]


y = int((b-a)+(c-b))

print (y)
