#9506번 약수들의 합
while(True):
    n = int(input())
    if n == -1 :
        break
    lst = []
    
    for i in range(1,n):
        if n % i == 0 :
            lst.append(i)
    if n == sum(lst) :
        print(n,"="," + ".join(str(i) for i in lst), sep=" ")
    else :
        print(n,"is NOT perfect.")