# 백준 연결 요소의 개수

'''
노드 개수 n과 에지 개수 m 입력받기
그래프 데이터 인접 리스트 graph 초기화
방문 기록 리스트 visited 초기화

def DFS() :
    visited에 노드 방문 기록
    if not visited[i] :
        방문한 노드와 인접한 노드 중 방문하지 않은 노드 DFS 실행 (재귀 함수로 구현)
    
for i in range(m) :
    graph 인접 리스트 저장
    
for i in range(1, n+1) :
    if not visited[i] :
        연결 요소 개수 1 증가
        DFS 실행

결과값 출력
'''

import sys

# 파이썬 깊이 제한 1000
# 깊이 설정 setrecursionlimit
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

result = 0

def DFS(i) :
    visited[i] = True
    for i in graph[i] :
        if not visited[i] :
            DFS(i)
            
for i in range(m) :
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    
for i in range(1, n+1) :
    if not visited[i] :
        result += 1
        DFS(i)
        
print(result)