n = input()
m = input()

x=''

for i in range(len(n)):
    if n[i]!=m[i]:
        x=x+'1'
    else:
        x=x+'0'
    
print(x)
