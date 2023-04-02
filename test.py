n, m = map(int, input().split())
room = [['X'] * (m+2) for _ in range(n+2)]

for i in range(1, n+1) :
    reserve = list(input())
    for j in range(1, m+1) :
        room[i][j] = reserve[j-1]
    
start, end = map(int, input().split())

check = [[0] * (m+2) for _ in range(n+2)]

def func(x, y, v) :
    if room[x][y] == 'O' :
        check[x][y] = func(x+1, y, v+1)
        return check[x][y]
    else :
        check[x][y] = 0
        return v
    
for i in range(1, n+1) :
    for j in range(1, m+1) :
        func(i, j, 0)

cnt = 0
noReverse = False
memory = False

for i in range(start, end) :
    if 'O' not in room[i] :
        noReverse = True

while not noReverse and start < end :
    
    start += max(check[start])
    
    if cnt == 0 and start >= end :
        memory = True
        break
    elif start < end :
        cnt += 1
  
if noReverse :
    print(-1)
else :
    if memory :
        print(0)
    else :
        print(cnt)

        