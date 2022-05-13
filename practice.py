import sys

input = sys.stdin.readline

n = int(input())
dp = []

for i in range(n) :
    dp.append(list(map(int, input().split())))

for i in range(1, n) :
    dp[i][0] = dp[i][0] + dp[i-1][0]
    dp[i][len(dp[i])-1] = dp[i-1][len(dp[i-1])-1] + dp[i][len(dp[i])-1]
    
    if len(dp[i]) >= 3:
        for j in range(1, (len(dp[i]) - 1)) :
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
            
print(max(dp[n-1]))