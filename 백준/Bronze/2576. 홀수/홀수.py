# 2576 : 홀수
lst = []
for i in range(7) :
    n = int(input())
    if n % 2 == 1 :    
        lst.append(n)
if lst :
    lst.sort()
    print(sum(lst))
    print(lst[0])
else :
    print(-1)