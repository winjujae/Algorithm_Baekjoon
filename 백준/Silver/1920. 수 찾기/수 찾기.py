#1920번 수 찾기(빠른 입출력)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0

import sys
input = sys.stdin.readline
n = input()
lst = list(map(int,input().split()))
lst.sort()
m = input()
lst_input = list(map(int,input().split()))
for j in lst_input :
    print(binary_search(lst,j))