# 직각삼각형_잼문제
while(True) :
    lst = list(map(int,input().split()))
    lst.sort(reverse=True)
    if lst[0]==0 and lst[1]==0 and lst[2]==0 :
        break
    elif lst[0]**2 == lst[1]**2 + lst[2]**2 :
        print("right")
    else :
        print("wrong")