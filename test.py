from collections import deque

n = int(input())
lock = list(map(int, input().split()))
firstLock = list(range(1,n+1))

rangeInx = []

def k_shift(k) :
    for i in range(k) :
        shiftVal = tmpLock.pop()
        tmpLock.insert(0, shiftVal)
    return tmpLock
        
def reverseRange(s, e) :
    tmp = tmpLock[s:e]
    
    for i in range(s, e) :
        val = tmp.pop()
        tmpLock[i] = val
    return tmpLock

# 뒤집기 구간 구하는 곳
for i in range(n-1) :
    diff = lock[i] - lock[i+1]
    if diff > 1 :
        rangeInx.append(i+1)

for i in range(1, n+1) :     # 첫번째 오른쪽 밀기
    j = 0
    s, e = rangeInx
    while j < 10 :
        if e+j >= n :
            break
        
        tmpLock = lock.copy()
        # print('backup', lock)
        j += 1
        tmpLock = k_shift(j)
        # print('first', tmpLock)
        reverseRange(s+j, e+j)
        k_shift(i)
        # print('second', tmpLock)
        
        if tmpLock == firstLock :
            break
    if tmpLock == firstLock :
            break

print(i+1)
print(s+j, e+j-1)
print(j-1)