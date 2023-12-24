# 1316번 그룹 단어 체커
n = int(input())
cnt = 0
for i in range(n) :
    lst = []
    str = input()
    for j in range(len(str)) :
        if j == 0 :
            lst.append(str[j])
            cnt_bi = 1
            continue
        if str[j] != str[j-1] :
            lst.append(str[j])
    for k in range(len(lst)) :
        if lst.count(lst[k]) >= 2 :
            cnt_bi = 0
    if cnt_bi == 1 :
        cnt += 1
print(cnt)