import sys

input = sys.stdin.readline

N = int(input())
result = 1
cnt = 0
def fac(result, cnt) :
    result *= (cnt+1)
    cnt += 1
    if cnt == N :
        return print(result)
    
    elif N == 0 :
        return print(result)
    
    else :
        fac(result, cnt)

fac(result, cnt)