# 5585 : 거스름돈
n = int(input())
def func(x) :
    x = 1000 - x
    cnt = 0
    while (x>0) :
        if x >= 500 :
            cnt += x // 500
            x = x % 500
        elif x >= 100 :
            cnt += x // 100
            x = x % 100
        elif x >= 50 :
            cnt += x // 50
            x = x % 50
        elif x >= 10 :
            cnt += x // 10
            x = x % 10
        elif x >= 5 :
            cnt += x // 5
            x = x % 5
        else :
            cnt += x
            x = 0
    return cnt
print(func(n))