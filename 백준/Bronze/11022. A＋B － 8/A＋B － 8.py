T = int(input())
k = []
a1 = []
b1 = []
for i in range(1,T+1):
    a, b = map(int,input().split())
    k.append(a + b)
    a1.append(a)
    b1.append(b)
for i in range(1,T+1):
    print("Case #{0}: {1} + {2} = {3}".format(i,a1[i-1],b1[i-1],k[i-1]))