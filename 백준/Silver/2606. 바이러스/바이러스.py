# 2606 : 바이러스
n = int(input())
line_cnt = int(input())
lst = [[] for _ in range(n+1)]
visited = [0] * (n + 1)

for i in range(line_cnt) :
    x,y = map(int,input().split())
    lst[x].append(y)
    lst[y].append(x)

# print(lst)
def func(x) :
    visited[x] = 1
    for i in lst[x] :
        if visited[i] == 0 :
            func(i)
func(1)
print(visited.count(1) - 1)