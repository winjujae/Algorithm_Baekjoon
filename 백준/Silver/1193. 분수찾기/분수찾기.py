# idx 1  3   6   10  15  21  28  36
# 값 1/1 2/1 1/3 4/1 1/5 6/1 1/7 8/1 ~
# 차이 1 2   3   4   5   6   7   8 ~

x = int(input())
lst = [1,1,1]
idx = 1
while(idx < x) :
    idx += lst[2]+1
    lst[2] += 1

if lst[2] % 2 == 0 :
    lst[0] = lst[2]
    lst[1] = 1
    for i in range(idx-x) :
        lst[0] -= 1
        lst[1] += 1
else :
    lst[0] = 1
    lst[1] = lst[2]
    for i in range(idx-x) :
        lst[0] += 1
        lst[1] -= 1    
print(str(lst[0])+"/"+str(lst[1]))