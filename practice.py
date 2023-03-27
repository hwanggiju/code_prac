# 백준 게임 개발 1516

'''
건물의 수 n 입력받기
건물 데이터 저장 인접 리스트 building 초기화하기
진입 차수 리스트 degree 생성하기
건물 짓는 데 걸리는 시간 저장 리스트 buildTime

for i in range(1, n+1) :
    n개의 입력받은 데이터 리스트로 받아오기
    인접 리스트 building 데이터 저장
    진입 차수 리스트 데이터 저장
    
큐 자료구조 q 생성하기

for i in range(1, n+1) :
    진입 차수 리스트 데이터가 0인 노드 큐에 삽입하기
    
각 건물이 위상 정렬 순으로 지어지는 걸리는 시간 저장 리스트 result 0으로 초기화

while q :
    q에서 데이터 하나씩 가져와 now 변수에 저장하기
    for next_ in building[now] :
        degree에서 next_ 노드 진입 차수 1 빼기
        max(result에 저장되있는 next_ 노드의 시간, now 노드에 저장돼있는 result 시간 + now 노드를 짓는 시간) result[next_] 시간 업데이트
        if degree[next_] == 0 :
            next_ 노드 q에 삽입하기
'''

from collections import deque

n = int(input())
building = [[] for _ in range(n+1)]
degree = [0] * (n+1)
buildTime = [0] * (n+1)

for i in range(1, n+1) :
    lst = list(map(int, input().split()))
    buildTime[i] = lst[0]
    idx = 1
    while True :
        if lst[idx] == -1 :
            break
        building[lst[idx]].append(i)
        degree[i] += 1
        idx += 1

q = deque()

for i in range(1, n + 1) :
    if degree[i] == 0 :
        q.append(i)
        
result = [0] * (n+1)
        
while q :
    now = q.popleft()
    for next_ in building[now] :
        degree[next_] -= 1
        result[next_] = max(result[next_], result[now] + buildTime[now])
        if degree[next_] == 0 :
            q.append(next_)

for i in range(1, n + 1) :
    print(result[i] + buildTime[i])