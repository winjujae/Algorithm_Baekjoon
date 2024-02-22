#1267번 핸드폰 요금
input()
lst=list(map(int,input().split()))
y, m = [],[]
for i in range(len(lst)) :
    y.append((lst[i]//30 + 1)*10)
    m.append((lst[i]//60 + 1)*15)
if sum(y) > sum(m) :
    print('M',sum(m))
elif sum(y) < sum(m) :
    print('Y',sum(y))
else :
    print('Y','M',sum(y))