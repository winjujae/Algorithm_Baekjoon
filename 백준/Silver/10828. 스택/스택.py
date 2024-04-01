#10828 스택
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque()
for i in range(n) :
    a = input().strip().split()
    if a[0] == 'push' :
        queue.append(a[1])
        continue
    if a[0] == 'pop' :
        if len(queue) == 0 :
            print(-1)
            continue
        print(queue[-1])
        queue.pop()
        continue
    if a[0] == 'size' :
        print(len(queue))
        continue
    if a[0] == 'empty' :
        if len(queue) == 0 :
            print(1)
            continue
        print(0)
        continue
    if a[0] == 'top' :
        if len(queue) == 0 :
            print(-1)
            continue
        print(queue[-1])