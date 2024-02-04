#10156번 과자
lst = list(map(int, input().split()))
if lst[0] * lst[1] > lst[2] :
    print(lst[0] * lst[1] - lst[2])
else :
    print(0)