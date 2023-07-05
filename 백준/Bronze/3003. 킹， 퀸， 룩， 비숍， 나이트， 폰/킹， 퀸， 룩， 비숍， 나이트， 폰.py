find = list(map(int,input().split()))
answer = [1, 1, 2, 2, 2, 8]
k = []
for i in range(6):
    k.append(answer[i] - find[i])
print(*k)