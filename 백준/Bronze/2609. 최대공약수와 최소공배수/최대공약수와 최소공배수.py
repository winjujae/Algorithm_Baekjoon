lst = list(map(int, input().split()))
max_sub = []
min_dub = []
# 24 -> 1 2 3 4 6 8 12 24
# 18 -> 1 2 3 6 9 18
sub = [[],[]]
for i in range(2) :
    for k in range(1,lst[i]+1) :
        if lst[i] % k == 0 :
            sub[i].append(k)
#print(sub)
myset = list(set(sub[0] + sub[1]))
for i in sub[0] :
    if i in sub[1] :
        max_sub.append(i)
print(max(max_sub))
#print(myset)
min_dub = []
for i in myset :
    if i == 1 :
        continue
    while(lst[0] % i == 0 and lst[1] % i == 0) :        
        min_dub.append(i)
        lst[0] = lst[0] // i
        lst[1] = lst[1] // i
min_dub = min_dub + [lst[0], lst[1]]
k = 1
for i in min_dub :
    k *= i
print(k)
# for i in range(1,min(lst)+1)) :
#     if max(lst) % i == 0 :
#         max_sub = i
