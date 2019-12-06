a = str(input())
b = str(input())

a = a.lower()
b = b.lower()

if a == b:
    print('0')
elif a < b:
    print('-1')
else:
    print('1')
