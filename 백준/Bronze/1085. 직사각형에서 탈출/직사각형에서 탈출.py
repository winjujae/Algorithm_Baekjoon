#1085번 직사각형 탈출
lst = list(map(int,input().split()))
#lst- 0 x , 1 y , 2 w , 3 h
print(min(lst[2]-lst[0],lst[0],lst[3]-lst[1],lst[1]))