n = int(input())
i = list(map(int, input().split()))
i.sort()
x = i[:1]
y = sum(x)
x1 = i[-1]
print (('EASY'*(abs(y-1)*abs(x1-1)))+('HARD')*(1-(abs(1-y)*abs(1-x1))))


