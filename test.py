from collections import deque 

def reverse(s, e) :
    tmpLst = q[s:e]
    idx = -1
    for i in range(s, e) :
        q[i] = tmpLst[idx]
        idx -= 1
    return q

##################### 입력받기 #####################
n = int(input())
lock = list(map(int, input().split()))
###################################################

q = deque()

for i in range(n) :
    q.append(lock[i])
    
secondShift = 0

for i in range(2, n) :
    if lock[i-1] - lock[i-2] != 1 :
        val = q.pop()
        q.appendleft(val)
        secondShift += 1
    else : break

if secondShift == 0 : 
    secondShift = n

q.appendleft(q[-1])
q.append(q[1])

tmp = 0
endIdx = -1

for i in range(1, n+1) :
    if q[i] - q[i-1] != 1 and q[i+1] - q[i] != 1 :
        tmp += 1
        endIdx = i
    
startIdx = endIdx - tmp + 1

q = list(q)
q = reverse(startIdx, endIdx+1)

firstShift = 0
for i in range(1, n+1) :
    if q[i] == 1 :
        firstShift = n + 1 - i
        break

print(firstShift)
print(startIdx, endIdx)
print(secondShift)
    
    
    