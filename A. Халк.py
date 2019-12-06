n = int(input())

s1 = 'I hate'
s2 = 'I love'
s3 = 'that'
s4 = ' it'
s = ''
y=1

for i in range(n):
    if y==1:
        s=s1+s4
        y+=1
    elif y%2==0:
        s=s.replace('it', '')
        s=s+s3+' '+s2+s4
        y+=1
    else:
        s=s.replace('it', '')
        s=s+s3+' '+s1+s4
        y+=1
print(s)
