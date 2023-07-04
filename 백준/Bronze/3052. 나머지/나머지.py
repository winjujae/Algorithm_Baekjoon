k = [int(input()) for i in range(10)]
k2 = []
a = 0
for i in range(10):
    k2.append(int(k[i] % 42))
    
k3 = set(k2)
a = len(k3)

print(a)