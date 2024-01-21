#2751번 수 정렬하기 2
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n) :
    lst.append(int(input()))
for i in sorted(lst) :
    print(i)