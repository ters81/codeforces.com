a = input()
b = input()
c = input()

s = []
for i in c:
    s.append(ord(i)-65)

count = [0]*26

for i in s:
    count[i] += 1

d = a + b
s1 = []
count1 = [0]*26

for i in d:
    s1.append(ord(i)-65)

for i in s1:
    count1[i] +=1

if count == count1:
    print('YES')
else:
    print('NO')
