n = int(input())

a, b, c = 0, 0, 0

for i in range(n):
    a1, b1, c1 = map(int, input().split())
    a+=a1
    b+=b1
    c+=c1

if a==0 and b==0 and c==0:
    print('YES')
else:
    print('NO')
