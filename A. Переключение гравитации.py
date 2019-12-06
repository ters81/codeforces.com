n = int(input())
a = list(map(int, input().split()))

count = [0]*max(max(a)+1, n)

for i in a:
    count[i] += 1

for i in range(max(max(a)+1, n)):
    if count[i] > 0:
        print((str(i)+' ') * count[i], end='')