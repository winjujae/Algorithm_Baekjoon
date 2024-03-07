#5543번 상근날드
lst = []
case = []
for i in range(5) :
    lst.append(int(input()))
for i in lst[:3] :
    for j in lst[3:] :
        case.append(i+j-50)
print(min(case))