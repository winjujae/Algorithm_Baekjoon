#1547번 공(야바위)
lst = [1,0,0]
for i in range(int(input())) :
    a,b = map(int, input().split())
    lst[a-1],lst[b-1] = lst[b-1],lst[a-1]
for i in range(3) :
    if lst[i] == 1 :
        print(i+1)
        break