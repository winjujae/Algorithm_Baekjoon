#2455 지능형 기차
lst1 = []
for i in range(4) :
    a, b = map(int,input().split())
    lst1.append(b-a)
k = 0
lst2 = []
for i in lst1 :
    k += i
    lst2.append(k)
print(max(lst2))