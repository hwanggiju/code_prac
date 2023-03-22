# 백준 DFS와 BFS

'''
노드의 개수 n, 에지 개수 m, 시작점 v 입력 받기
graph 인접 리스트 저장
visited 방문 기록 초기화

for i in range(m) :
    graph 인접 리스트에 저장하기

for i in graph :
    인접 리스트 오름차순 정렬 -> 이유 : 노드가 작은 것부터 방문하기 위해서

def DFS(v) :
    현재 노드 출력하기
    visited에 현재 노드 방문 기록하기
    현재 노드에서 인접 노드에 방문하지 않은 노드가 있다면 DFS 수행하기
    
DFS(v) 실행

def BFS(v) :
    큐 자료구조 q 생성하기
    visited에 현재 노드 방문 기록하기
    while q :
        q에서 가장 먼저 들어온 데이터 가져오기
        가져온 데이터 출력하기
        가져온 데이터와 인접한 노드 큐에 저장하고 visited 방문 기록하기

visited 초기화
BFS(v) 실행
'''

from collections import deque

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m) :
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in graph :
    i.sort()

def DFS(v) :
    print(v, end=' ')
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            DFS(i)
            
DFS(start)

def BFS(v) :
    q = deque()
    q.append(v)
    visited[v] = True
    while q :
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now] :
            if not visited[i] :
                visited[i] = True
                q.append(i)
                
print()
visited = [False] * (n+1)
BFS(start)
