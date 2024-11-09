# 7568 : 덩치
n = int(input())
lst = []
rank = [1] * n

for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))

for i in range(n) :
    for j in range(n) :
        if i != j :
            if lst[j][0] > lst[i][0] and lst[j][1] > lst[i][1] :
                rank[i] += 1
        
print(" ".join(map(str,rank)))
