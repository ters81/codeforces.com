n = int(input())

s=0
maximum=0

for i in range(n):
    a, b = map(int, input().split())
    if s>=0:
        s=s-a+b
        if s>maximum:
            maximum=s
print(maximum)
    
