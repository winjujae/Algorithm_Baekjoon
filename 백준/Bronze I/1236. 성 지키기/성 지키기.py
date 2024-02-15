#1236번 성지키기
n, m = map(int, input().split())
lst = [list('.' for _ in range(m)) for _ in range(n)]
for i in range(n) :
    lst[i] = input()
#print(lst)
cnt = 0
p,q = [],[]
for i in range(n) :
    if 'X' in lst[i] :
        continue
    else :
        p.append(i)

for j in range(m) : # 5열
    temp = []
    for i in range(n) : # 3행
        temp.append(lst[i][j])
    if 'X' in temp :
        continue
    else :
        q.append(j)
#print(p,q)
print(max(len(p),len(q)))