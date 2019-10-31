s = input()
s1 = ' '+s

a = s1.find('h')
a1 = int(a/abs(a))

b = s1.find('e',(a+1))
b1 = int(b/abs(b))

c = s1.find('l',(b+1))
c1 = int(c/abs(c))

d = s1.find('l',(c+1))
d1 = int(d/abs(d))

e = s1.find('o',(d+1))
e1 = int(e/abs(e))

x = a1 + b1 + c1 + d1 + e1 + 1

x1 = int(x/6)
x2 = abs(x1-1)

print(('YES'*x1)+('NO'*x2))
