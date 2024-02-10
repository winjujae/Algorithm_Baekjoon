#5717번 상근이의 친구들
while(True) :
    lst = list(map(int, input().split()))
    if lst[0] == 0 and lst[1] == 0 :
        break
    print(lst[0] + lst[1])