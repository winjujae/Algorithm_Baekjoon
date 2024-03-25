#11866번 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())

ys = []  # 뽑은 수 넣을 요세푸스 리스트
queue = []
idx = 0
for i in range(1, n + 1):
    queue.append(i)

while queue: # queue가 비어있다면 실행종료(false)
    idx += k - 1
    if idx >= len(queue) :
        idx %= len(queue)
    ys.append(str(queue.pop(idx)))

print("<", end="")
print(", ".join(map(str, ys)), end="")
print(">")