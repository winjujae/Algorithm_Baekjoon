while(True) :
    lst = list(map(int,input().split()))
    if lst[0] == 0 and lst[1] == 0 :
        break
    if lst[1] % lst[0] == 0 :
        print("factor")
    elif lst[0] % lst[1] == 0 :
        print("multiple")
    else :
        print("neither")