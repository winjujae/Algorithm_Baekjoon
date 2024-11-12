# 1003 : 피보나치 함수
dp = [(1, 0), (0, 1)]

def fibo_count(x):
    if len(dp) <= x :
        for i in range(len(dp), x + 1):
            zero_count = dp[i - 1][0] + dp[i - 2][0]
            one_count = dp[i - 1][1] + dp[i - 2][1]
            dp.append((zero_count, one_count))
    return dp[x]

n = int(input())
for _ in range(n):
    x = int(input())
    result = fibo_count(x)
    print(result[0], result[1])