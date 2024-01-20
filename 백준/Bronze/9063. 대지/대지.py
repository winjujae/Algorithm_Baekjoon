#9063번 대지
n = int(input())
lst = [list(map(int,input().split())) for i in range(n)]
lst_x = []
lst_y = []
for i in range(len(lst)) :
    lst_x.append(lst[i][0])
    lst_y.append(lst[i][1])
#print(lst_x,lst_y)
print((max(lst_x)-min(lst_x)) * (max(lst_y)-min(lst_y)))