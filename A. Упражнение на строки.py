a = input()

x = 'aoyeui'
y=''

a=a.lower()

for i in range(len(a)):
    if a[i] not in x:
        y=y+a[i]
y=y.replace('','.')

print(y[0:-1])
        
