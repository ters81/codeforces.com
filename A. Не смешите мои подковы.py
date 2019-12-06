s = list(map(int, input().split()))

x = []

for i in range(len(s)):
    if s[i-1] not in x:
        x.append(s[i-1])
print(len(s)-len(x))
