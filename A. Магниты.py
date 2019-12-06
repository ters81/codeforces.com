n = int(input())
a = input()

s=1

for i in range(n-1):
    b = input()
    if b==a:
        a=b
        s=s+0
    else:
        a=b
        s+=1

print(s)
