# 백준 - 최단 경로 1753

'''
노드 개수 n과 에지 개수 e 입력 받기
출발 노드 startNode 입력받기
인접 리스트 graph 초기화하기
최단 경로 리스트 path 초기화하기 
방문 리스트 visited 초기화하기

for i in range(1, m+1) :
    출발점 u, 도착점 v, 가중치 w 입력받기
    출발점의 인접 리스트 데이터 업데이트
    최단 경로 리스트 가중치 업데이트
    
우선순위 큐 자료구조 q 생성하기
(출발 노드 가중치 0, 출발 노드) q 추가하기
while q :
    q 데이터 now 가져오기
    가져온 노드 nowNode에 저장하기
    
    if visited[nowNode] :
        continue
    
    visited[nowNode] = True
    
    for i in graph[nowNode] :.
        인접 노드 nextNode에 저장
        가중치 데이터 val에 저장
        if path[nextNode] > path[nowNode] + val :
            path 경로에 최소 경로 데이터로 업데이트
            (인접 노드의 가중치, 인접 노드) q에 넣어주기
            
for i in range(1, n+1) :
    if visited[i] :
        최종 path 경로 출력하기
    else :
        INF 출력하기
'''

from queue import PriorityQueue
import sys

input = sys.stdin.readline

n, e = map(int, input().split())
startNode = int(input())

graph = [[] for _ in range(n + 1)]
path = [sys.maxsize] * (n + 1)
visited = [False] * (n+1)

path[startNode] = 0

for i in range(e) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
q = PriorityQueue()
q.put((0,startNode))

while q.qsize() > 0 :
    now = q.get()
    nowNode = now[1]
    
    if visited[nowNode] :
        continue
    
    visited[nowNode] = True
    
    for i in graph[nowNode] :
        nextNode = i[0]
        val = i[1]
        if path[nextNode] > path[nowNode] + val :
            path[nextNode] = path[nowNode] + val
            q.put((path[nextNode], nextNode))
            
for i in range(1, n+1) :
    if visited[i] :
        print(path[i])
    else :
        print('INF')