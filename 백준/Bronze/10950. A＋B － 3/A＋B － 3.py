T = int(input())
k = []
for i in range(1,T+1):
    a, b = map(int,input().split())
    k.append(a + b)
for i in range(1,T+1):
    print(k[i-1])