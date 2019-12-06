k, n, w = map(int, input().split())

s=0
q=1

for i in range(w):
    s=s+k*q
    q+=1    
    
x=s-n

if x>0:
    print(x)
else:
    print('0')
