# 백준 트리의 지름

'''
노드 개수 n 입력받기
graph 인접 리스트 입력받고 저장하기
for i in range(n) :
    graph 인접 리스트 정보 입력받기
    
visited 방문 기록 리스트 초기화하기
distance 거리 리스트 초기화하기

def BFS(v) :
    큐 자료구조 생성하기
    visited 방문 기록하기
    while q :
        큐 자료구조에서 가장 앞에 있는 데이터 가져오기 now
        for i in graph[now] :
            if not visited[i[0]] :
                i[0]의 인덱스에서 visited 방문 기록하기
                큐 자료구조에 i[0] 노드 추가하기
                큐 자료구조에 삽입된 노드 거리는 현재 거리값 + 에지 거리값

BFS(임의의 노드 시작점) 실행하기
거리 최대값 인덱스 초기화 max_
distance 리스트에서 가장 큰 값을 가지는 인덱스 max_ 업데이트하기

distance 리스트 초기화하기
visited 리스트 초기화하기

BFS(max_)
distance 오름차순 정렬하기
distance의 가장 큰 수 출력하기
'''

from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n) :
    tmp = list(map(int, input().split()))
    idx = 0
    node = tmp[idx]
    idx += 1
    while True :
        endNode = tmp[idx]
        if endNode == -1 :
            break
        val = tmp[idx+1]
        graph[node].append((endNode, val))
        idx += 2
        
visited = [False] * (n+1)
distance = [0] * (n+1)

def BFS(v) :
    q = deque()
    q.append(v)
    visited[v] = True
    while q :
        now = q.popleft()
        for i in graph[now] :
            if not visited[i[0]] :
                visited[i[0]] = True
                q.append(i[0])
                distance[i[0]] = distance[now] + i[1]
                
BFS(1)
max_ = 1

for i in range(2, n+1) :
    if distance[max_] < distance[i] :
        max_ = i
        
visited = [False] * (n+1)
distance = [0] * (n+1)

BFS(max_)
distance.sort()
print(distance[n])