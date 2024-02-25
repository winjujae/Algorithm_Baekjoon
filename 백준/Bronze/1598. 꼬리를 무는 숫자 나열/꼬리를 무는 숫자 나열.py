#1598번 꼬리를 무는 숫자 나열
lst = list(map(int, input().split()))
lst[0] -= 1
lst[1] -= 1
print(abs(lst[0]//4 - lst[1]//4) + abs(lst[0]%4 - lst[1]%4))