n = int(input())

count=0
x=1
y=1

while n>0 and x<=n:
    count+=1
    n=n-x
    y+=1
    x=x+y
    
print(count)
