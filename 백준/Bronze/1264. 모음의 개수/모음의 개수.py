#1264번 모음의개수
while(True) :
    lst = list(input().split())
    if lst == ['#'] :
        break
    cnt = 0
    for i in range(len(lst)) :
        for j in lst[i].lower() :
            if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u' :
                cnt += 1
    print(cnt)