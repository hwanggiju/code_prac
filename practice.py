import sys

input = sys.stdin.readline

def f(N, start, end) :
    if N == 1:
        print(start, end)
        return
    
    f(N - 1, start, 6 - start - end)
    print(start, end)
    f(N - 1, 6 - start - end, end)

N = int(input()) # 원판개수
print(2**N - 1)
f(N, 1, 3)