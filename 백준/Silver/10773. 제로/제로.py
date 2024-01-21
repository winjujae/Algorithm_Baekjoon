#10773번 제로
n = int(input())
lst = []
for i in range(n) :
    k = int(input())
    if k == 0 :
        lst.pop()
    else :
        lst.append(k)
    #print(lst)
print(sum(lst))