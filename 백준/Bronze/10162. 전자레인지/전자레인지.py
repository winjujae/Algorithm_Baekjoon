# 10162 : 전자레인지
n = int(input())
def func(x) :
    a,b,c = 0,0,0
    if x % 10 != 0 :
        return -1
    if x // 300 >= 1 :
        a = x // 300
        x = x % 300
    if x // 60 >= 1 :
        b = x // 60
        x = x % 60
    c = x // 10
    x = x % 10
    return a, b, c
if func(n) == -1 :
    print(-1)
else :
    print(" ".join(map(str, func(n))))