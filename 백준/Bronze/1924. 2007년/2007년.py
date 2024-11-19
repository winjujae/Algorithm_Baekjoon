# 1924 : 2007년
n,m = map(int,input().split())
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

temp = sum(month[:n]) + m
ans = temp % 7
print(day[ans])