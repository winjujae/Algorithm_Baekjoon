# 15596 : 정수 N개의 합
from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1,n+1)])
temp_lst = []
cnt = 0

while queue:
    queue.rotate(-(k - 1)) # 순환 rotate
    temp_lst.append(queue.popleft())

#print(temp_lst)
print("<" + ", ".join(map(str,temp_lst)) + ">")