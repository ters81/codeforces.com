a, b = map(int, input().split())

count=0
x=1

while x<=a:
    count+=1
    if x%b==0:
        a+=1
    x+=1
    
print(count)
