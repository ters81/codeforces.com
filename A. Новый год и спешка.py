n, k = map(int, input().split())

x=240-k
count=0
y=1

while x>=y*5 and y<=n:
    count+=1
    x=x-y*5
    y+=1
   
print(count)
