#11945번 뜨거운 붕어빵
n,m = map(int,input().split())
lst = []
for i in range(n) :
    lst.append(input())
for i in range(len(lst)) :
    print(lst[i][::-1])