while(True) :
    lst= list(map(int,input().split()))
    if lst[0] == 0 and lst[1] == 0 :
        break
    elif lst[0] > lst[1] :
        print("Yes")
    else :
        print("No")