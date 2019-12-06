a = str(input())
b = str(input())

a = a.lower()
b = b.lower()

if a != b:
    if a < b:
        print('-1')
    else:
        print('1')
else:
    print('0')
