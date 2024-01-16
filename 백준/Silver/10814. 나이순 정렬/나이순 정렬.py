n = int(input())
lst = [list(input().split()) for i in range(n)]

for i in range(len(lst)):
    lst[i][0] = int(lst[i][0])

lst.sort(key=lambda x: x[0])

for i in range(len(lst)):
    print(lst[i][0], lst[i][1])