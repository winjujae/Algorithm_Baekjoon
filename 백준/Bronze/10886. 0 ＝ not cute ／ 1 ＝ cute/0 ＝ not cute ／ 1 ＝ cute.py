n = int(input())
k = 0
for i in range(n) :
    if int(input()) == 0 :
        k += 1
if k > n/2 :
    print("Junhee is not cute!")
else :
    print("Junhee is cute!")