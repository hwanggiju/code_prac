# 백준 ABCDE

'''
사람 수 n, 에지 수 m 입력받기
그래프 리스트 graph 초기화하기
방문 기록 리스트 visited 초기화하기
깊이 도착 확인 변수 finish

def DFS(현재 값, 깊이) :
    if 깊이 == 5 :
        finish = True
        return
    visited[현재 값] = True
    for i in graph[현재 값] :
        방문하지 않은 노드 DFS 수행

for i in range(m) :
    graph 인접 리스트 데이터 저장
    
for i in range(n) :
    DFS(i, 1) 실행
    if (finish) :
        반복 종료
        
if finish :
    1 출력하기
else : 
    0 출력하기
'''

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

finish = False

def DFS(val, depth) :
    global finish
    if depth == 5 :
        finish = True 
        return
    visited[val] = True
    for i in graph[val] :
        if not visited[i] :
            DFS(i, depth + 1)
    visited[val] = False
        
for i in range(m) :
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(n) :
    DFS(i, 1)
    if finish :
        break
    
if finish :
    print(1)
else :
    print(0)
            