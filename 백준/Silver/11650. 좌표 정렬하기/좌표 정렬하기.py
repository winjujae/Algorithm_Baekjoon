#11650번 좌표 정렬하기
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
#print(lst)
lst.sort(key=lambda x : (x[0],x[1]))
#print(lst)
for i in range(n) :
    print(lst[i][0],lst[i][1])