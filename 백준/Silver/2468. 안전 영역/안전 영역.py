from sys import *

setrecursionlimit(10 ** 6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
num = int(input())
input_list = []
value = 0
result = 0

for i in range(num):
    input_list.append(list(map(int, input().split())))

def dfs(y, x, high):
    visit[y][x] = False

    for i in range(4):
        dir_y = y + dy[i]
        dir_x = x + dx[i]
        if dir_x > -1 and dir_x < num and dir_y < num and dir_y > -1:
            if visit[dir_y][dir_x] and input_list[dir_y][dir_x] > high:
                dfs(dir_y, dir_x, high)

for high in range(101):
    visit = [[True] * num for i in range(num)]
    value = 0
    for i in range(num):
        for j in range(num):
            if visit[i][j] == True and input_list[i][j] > high:
                value += 1
                dfs(i, j, high)
    result = max(result, value)
    if value == 0:
        break

print(result)