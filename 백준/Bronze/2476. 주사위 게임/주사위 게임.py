#2476번 주사위게임
prize = 0
for _ in range(int(input())) :
    lst = list(map(int, input().split()))
    if lst.count(lst[0]) == 3 :
        k = 10000 + (lst[0]*1000)
    elif lst.count(lst[0]) == 2 :
        k = 1000 + (lst[0]*100)
    elif lst.count(lst[1]) == 2 :
        k = 1000 + (lst[1]*100)
    else :
        k = max(lst)*100
    if prize < k :
        prize = k
print(prize)