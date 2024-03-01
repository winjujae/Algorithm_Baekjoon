#2083번 럭비 클럽
while(True) :
    lst = list(input().split())
    if lst[0] == '#' and int(lst[1]) == 0 and int(lst[2]) == 0 :
        break
    if int(lst[1]) >= 18 or int(lst[2]) >= 80 :
        print(lst[0],'Senior')
    else :
        print(lst[0],'Junior')