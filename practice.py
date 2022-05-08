import sys

input = sys.stdin.readline

T = int(input())
Tc = []

for i in range(T) :
    Tc.append(int(input()))

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
def P(n) :
    if n == 5 :
        dp[n] = dp[n-1]
    if dp[n] == 0 :
        dp[n] = dp[n-5] + dp[n-1]
    return dp[n]

for i in Tc :
    for j in range(4, i+1) :
        P(j)
    print(dp[i])