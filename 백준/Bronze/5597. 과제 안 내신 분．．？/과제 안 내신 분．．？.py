k = [i for i in range(1,31)]

for i in range(28) :
    num = int(input())
    k.remove(num)
print(min(k))
print(max(k))