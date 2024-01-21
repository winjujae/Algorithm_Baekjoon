## 2775번 부녀회장이 될테야
# 1 층
# 4 호
# 0 층 - 1 2 3 4 호 의 합
# 1 + 2 + 3 + 4 = 10

# 2 층
# 4 호
# 1 층 - 1 2 3 4 호의 합
# 0층 ( 1 + 2 + 3 + 4 ) -> 1층 ( 1 + 3 + 6 + 10 ) = 20

t= int(input())
for _ in range(t) :
    k = int(input()) # 층 0부터
    n = int(input()) # 호 1부터
    start_lst = list(i for i in range(1,n+1))
    
    for i in range(k) :
        for j in range(1,n) :
           start_lst[j] += start_lst[j-1]
        #print(start_lst)
    print(start_lst[-1])