n = int(input())

M=0
C=0
F=0

for i in range(n):
    m, c = map(int, input().split())
    if m>c:
        M+=1
    elif c>m:
        C+=1
    
if M>C:
    print('Mishka')
elif C>M:
    print('Chris')
else:
    print('Friendship is magic!^^')
