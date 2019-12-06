n = int(input())
a = str(input())

A = a.count('A')
D = a.count('D')

if A>D:
    print('Anton')
elif A<D:
    print('Danik')
else:
    print('Friendship')
