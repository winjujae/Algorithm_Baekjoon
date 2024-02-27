#5532번 방학 숙제
lst = []
for i in range(5) :
    lst.append(int(input()))
print((lst[0] - max((lst[1]-1)//lst[3]+1 , (lst[2]-1)//lst[4]+1)))