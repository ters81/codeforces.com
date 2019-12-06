n = int(input())

A=0

for i in range(n):
    a = input()
    if a=='++X' or a=='X++':
        A+=1
    else:
        A=A-1

print(A)
