n = int(input())
t = list(map(int, input().split()))

if t.count(1)>0 and t.count(2)>0 and t.count(3)>0:
    x = min(t.count(1),t.count(2),t.count(3))               
    print(x)

    for i in range(x):
        print(t.index(1)+1, t.index(2)+1, t.index(3)+1)
        a=t.index(1)
        t.remove(1)
        t.insert(a,0)
        a=t.index(2)
        t.remove(2)
        t.insert(a,0)
        a=t.index(3)
        t.remove(3)
        t.insert(a,0)
else:
    print('0')
