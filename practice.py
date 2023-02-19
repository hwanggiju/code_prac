# 미로 탈출
from collections import deque

def bfs(start, end, maps) :
    tmp = [[0]*100 for _ in range(100)] 
    q = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    for i in range(len(maps)) :
        for j in range(len(maps[0])) :
            if maps[i][j] == start :
                q.append([i, j, 0])
    
    while q :
        val = q.popleft()
        if maps[val[0]][val[1]] == end :
            return val[2]
        
        for k in range(4) :
            x = val[1] + dx[k]
            y = val[0] + dy[k]
            if x >= len(maps[0]) or y >= len(maps) or x < 0 or y < 0 :
                pass
            elif maps[y][x] == 'X' :
                pass
            elif tmp[y][x] != 0 :
                pass
            else :
                q.append([y, x, val[2]+1])
                tmp[y][x] = 1
                
    return -1
        
            
def solution(maps):
    answer = 0
    a = bfs('S', 'L', maps)
    b = bfs('L', 'E', maps)
    print(a)
    print(b)
    if a == -1 or b == -1 :
        return -1
    else :
        answer = a + b
    return answer