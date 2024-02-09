lst = []
for i in range(5):
    k = int(input())
    if k < 40 :
        k = 40
    lst.append(k)
print(sum(lst)//len(lst))