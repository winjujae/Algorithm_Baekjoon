#1247번 부호
import sys
for _ in range(3) :
    a = 0
    for i in range(int(input())) :
        a += int(sys.stdin.readline().strip())
    if a == 0 :
        print(0)
    elif a < 0 :
        print('-')
    else :
        print('+')