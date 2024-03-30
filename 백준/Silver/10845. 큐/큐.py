#10845번 큐
from collections import deque
import sys
queue = deque()
input = sys.stdin.readline
n = int(input())
for i in range(n) :
    a = input().strip().split()
    if a[0] == 'push' :
        queue.append(int(a[1]))
        continue
                
    if a[0] == 'pop' :
        if len(queue) == 0 :
            print(-1)
            continue
        print(queue[0])
        queue.popleft()
        continue
        
    if a[0] == 'front' :
        if len(queue) == 0 :
            print(-1)
            continue
        print(queue[0])
        continue
        
    if a[0] == 'back' :
        if len(queue) == 0 :
            print(-1)
            continue
        print(queue[-1])
        continue
        
    if a[0] == 'size' :
        print(len(queue))
        continue

    if a[0] == 'empty' :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
        continue