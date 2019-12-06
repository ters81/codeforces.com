n, m = map(int,input().split())

count = 0
x=1
while x<=n:
    count+=1                    
    if x%m==0:      
        n=n+1       
    
    x=x+1            

print(count)
