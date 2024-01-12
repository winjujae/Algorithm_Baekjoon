lst = list(map(int,input().split()))
n_lst = []
for i in range(1,lst[0]+1):
    if lst[0] % i == 0 :
        n_lst.append(i)
if len(n_lst) < lst[1] :
    print("0")
else :
    print(n_lst[lst[1]-1])