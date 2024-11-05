# 2750 : 수 정렬하기
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
for i in range(len(lst)) :
    print(lst[i])