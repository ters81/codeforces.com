n,m,a,b = map(int,input().split())

x = a*n
y = (n//m)*b
z = n-m*(n//m)
q = z*a
q1 = y+q

w = (n//m)+1
w1 = w*b

print(min(x, q1, w1))
