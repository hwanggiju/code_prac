# 백준 - K번째 최단 경로 찾기 1854

import sys
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())     # n 도시 수, m 도로 수, k 찾을 경로
graph = [[] for _ in range(n + 1)]      # 인접 리스트 graph 생성
path = [[sys.maxsize] * k for _ in range(n + 1)]    # 최단 경로 2차원으로 생성
# 같은 노드를 방문할 수 있기 때문에 방문 리스트 x

# 인접 리스트 graph 초기화하기
for i in range(m) :
    a, b, c = map(int, input().split()) # a 출발, b 도착, c 걸리는 시간
    graph[a].append((b, c))

hpq = [(0, 1)] # (가중치, 출발 노드)
path[1][0] = 0

while hpq :
    weight, node = heapq.heappop(hpq)
    for i in graph[node] :
        nextNode = i[0]     # 인접 노드
        addWeight = i[1]    # 인접 리스트 가중치
        sumWeight = weight + addWeight
        
        if path[nextNode][k-1] > sumWeight :    # k-1번째 값 비교
            path[nextNode][k-1] = sumWeight     # nextNode 행 k-1
            path[nextNode].sort()               # k번째 최단 경로를 구하기 위해서 정렬
            heapq.heappush(hpq, (sumWeight, nextNode))  # 업데이트 시 새로운 경로 삽입하기

for i in range(1, n+1) :
    if path[i][k-1] == sys.maxsize :
        print(-1)
    else :
        print(path[i][k-1])
    
    