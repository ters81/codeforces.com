x = int(input())

y=0

while x>0:
    last=x%2
    y=y+last
    x=x//2
print(y)
