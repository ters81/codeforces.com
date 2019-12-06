n = int(input())
a = input()
b = input()

s=0

for i in range(n):
    if abs(int(a[i])-int(b[i]))<=5:
        s=s+abs(int(a[i])-int(b[i]))
    else:
        s=s+(10 - max(int(a[i]),int(b[i]))) + min(int(a[i]),int(b[i]))
             
print(s)
