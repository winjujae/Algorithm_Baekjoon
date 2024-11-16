# 2579 : 계단 오르기
n = int(input())
lst = [0]
for i in range(n) :
    lst.append(int(input()))
    
dp = [0] * (n+1)

dp[1] = lst[1]
if n > 1:
    dp[2] = lst[1] + lst[2]
    
for i in range(3, n + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + lst[i - 1]) + lst[i]
print(dp[n])