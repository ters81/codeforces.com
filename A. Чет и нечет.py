a, b = map(int, input().split())

if a%2==0:
    if b <= a/2:
        print(b+(b-1))
    else:
        print(int(b-a/2)*2)
else:
    a = a+1
    if b <= a/2:
        print(b+(b-1))
    else:
        print(int(b-a/2)*2)
