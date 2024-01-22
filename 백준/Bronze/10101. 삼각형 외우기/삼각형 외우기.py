#10101번 삼각형 외우기
lst = [int(input()) for i in range(3)]
lst.sort()
if lst[0] == lst[1] == lst[2] == 60 :
    print("Equilateral")
elif sum(lst) == 180 :
    if lst[0] == lst[1] or lst[1] == lst[2] or lst[2] == lst[0] :
        print("Isosceles")
    else :
        print("Scalene")
else :
    print("Error")