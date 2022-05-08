import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2

def f(n) :
    if dp[n] == 0 :
        dp[n] = (dp[n-1] + dp[n-2]) % 15746
        return dp[n]

for i in range(3, N + 1) :
    f(i)

print(dp[N])