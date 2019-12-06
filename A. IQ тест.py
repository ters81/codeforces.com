n = int(input())
a = list(map(int,input().split()))

chet=[]
nechet=[]


for i in range(n):
    if a[i]%2==0:
        chet.append(a[i])
    else:
        nechet.append(a[i])
        
if len(chet)>len(nechet):
    print(a.index(nechet[0])+1)

else:
    print(a.index(chet[0])+1)
