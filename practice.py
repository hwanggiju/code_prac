# 프로그래머스 게임 맵 최단 거리
from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    visited = [[False] * m for _ in range(n)]
    
    def bfs(x, y) :
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        while q :
            now = q.popleft()
            for i in range(4) :
                X = now[0] + dx[i]
                Y = now[1] + dy[i]
                if X >= 0 and Y >= 0 and X < n and Y < m :
                    if maps[X][Y] != 0 and not visited[X][Y] :
                        visited[X][Y] = True
                        maps[X][Y] = maps[now[0]][now[1]] + 1
                        q.append((X, Y))
    bfs(0, 0)
    answer = maps[n-1][m-1]
    if maps[n-1][m-1] == 1 :
        answer = -1
    return answer