T = int(input())
k = []
for i in range(1,T+1):
    a, b = map(int,input().split())
    k.append(a + b)
for i in range(1,T+1):
    print("Case #{0}: {1}".format(i,k[i-1]))