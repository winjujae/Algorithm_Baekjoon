#3009번 네번째 점
lst_1 = list(map(int,input().split()))
lst_2 = list(map(int,input().split()))
lst_3 = list(map(int,input().split()))
lst = [[],[]]
lst[0] = [lst_1[0],lst_2[0],lst_3[0]]
lst[1] = [lst_1[1],lst_2[1],lst_3[1]]

for i in lst[0] :
    if lst[0].count(i) == 1 :
        a = i
        break
for j in lst[1] :
    if lst[1].count(j) == 1 :
        b = j
        break
print(a, b)