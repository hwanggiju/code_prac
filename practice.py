# 백준 미로 탐색

'''
상하좌우를 탐색하기 위한 dx, dy 리스트 정의
미로에서 행 개수 n과 열 개수 m 입력받기
미로 데이터 map_ 입력받기 - 2차원
방문 리스트 visited 생성하고 초기화하기 - 2차원

def BFS(x, y) :
    큐 자료구조 q 생성하기
    시작점 데이터 q 입력하기
    x, y visited 방문 기록하기
    while q :
        q에서 가장 앞에 있는 데이터 가져오기 now
        for i in range(4) :
            상하좌우 좌표값 위치 dx, dy를 통해 X, Y 계산하기
            if X >= 0 and Y >= 0 and X < n and Y < m :
                if not visited[X][Y] and map_[X][Y] != 0 :
                    visited 리스트 방문 기록하기
                    map_ 리스트에 현재 노드 데이터의 + 1 로 업데이터 -> 깊이 계산
                    q.appned((X, Y))
                    
BFS((0, 0))
목적지 좌표 출력하기     
'''

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n , m = map(int, input().split())
map_ = [[0] * m for _ in range(n)]
for i in range(n) :
    num = list(input())
    for j in range(m) :
        map_[i][j] = int(num[j])

visited = [[False] * m for _ in range(n)]

def BFS(x, y) :
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q :
        now = q.popleft()
        for i in range(4) :
            X = now[0] + dx[i]
            Y = now[1] + dy[i]
            if X >= 0 and Y >= 0 and X < n and Y < m :
                if map_[X][Y] != 0 and not visited[X][Y] : 
                    visited[X][Y] = True
                    map_[X][Y] = map_[now[0]][now[1]] + 1
                    q.append((X, Y))
                
BFS(0, 0)
print(map_[n-1][m-1])