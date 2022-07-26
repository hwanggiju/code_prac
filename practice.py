import sys

N = int(input())
dp = [[0 for i in range(10)] for j in range(101)]

# 1, 2, 3, 4, 5, 6, 7, 8, 9
# 1 2, 2 1, 2 3, 3 2, 3 4, 4 3, 4 5, 5 4, 5 6, 6 5, 6 7,
# 7 6, 7 8, 8 7, 8 9, 9 8
for i in range(1, 10) :
    dp[1][i] = 1

for i in range(2, N+1) :
    for j in range(10) :
        if j == 0 :
            dp[i][j] = dp[i-1][1]
        elif j == 9 :
            dp[i][j] = dp[i-1][8]
        else :
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(dp)            
print(sum(dp[N]) % 1000000000)
    