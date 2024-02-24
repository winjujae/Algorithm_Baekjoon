#4470번 줄번호
n = int(input())
lst = [input() for i in range(n)]
for i in range(n) :
    print('{0}. {1}'.format(i+1,lst[i]))