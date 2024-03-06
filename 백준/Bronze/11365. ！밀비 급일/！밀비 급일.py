#11365번
while(True) :
    k = input()
    if k == 'END' :
        break
    a = ''
    for i in k[::-1] :
        a += i
    print(a)