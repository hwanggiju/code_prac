# 백준 최솟값 찾기

'''
데이터의 개수 n과 슬라이딩 윈도우 크기 L 입력받기
덱 자료구조 dq 생성하기
n개의 데이터 dataLst에 저장하기

for i in range(n) :
    while dq and dq[-1][0] > dataLst[i] :
        덱의 마지막 노드 데이터부터 현재 새로운 노드 데이터보다 큰 값은 제거
    덱에 (데이터, 인덱스) 형태의 노드 추가
    if len(dq) > L :
        윈도우의 범위보다 덱의 길이가 크다면, 가장 앞의 노드를 제거
    덱의 가장 앞 노드 데이터 최솟값 출력
'''

from collections import deque

n, L = map(int, input().split())
dq = deque()
dataLst = list(map(int, input().split()))

for i in range(n) :
    while dq and dq[-1][0] > dataLst[i] :
        dq.pop()
        
    dq.append((dataLst[i], i))
    
    if  dq[0][1] <= i-L :
        dq.popleft()
        
    print(dq[0][0], end=' ')
    