#5575번 타임 카드
for _ in range(3) :
    lst = list(map(int, input().split()))
    start_s = lst[0] * 3600 + lst[1] * 60 + lst[2]
    end_s = lst[3] * 3600 + lst[4] * 60 + lst[5]
    k = end_s - start_s
    print(k//3600,(k//60)%60,k%60)