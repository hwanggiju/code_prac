import sys

input = sys.stdin.readline

T = int(input())
cnt = [[0, 0] for i in range(41)]
tc = [int(input()) for i in range(T)]

cnt[0] = [1, 0]
cnt[1] = [0, 1]

def fibo(n) :
    if cnt[n] == [0, 0] :
        cnt[n] = [x+y for x,y in zip(fibo(n-1), fibo(n-2))]
        return cnt[n]

    else :
        return cnt[n]

for i in tc :
    fibo(i)
    print(*cnt[i])