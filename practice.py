# 백준 집합의 표현 1717

'''
노드 개수 n과 질의 횟수 m 입력받기
대표 노드 리스트 preNode 초기화

def unoin(a, b) :
    a, b의 대표 노드 확인
    if a != b :
        b의 노드에 대표 노드 a 업데이트
        
def find(v) :
    if preNode[v] == v:
        대표 노드인 v를 반환
    else :
        preNode[v]는 find(preNode[v]) 호출 후 속해있는 집합의 대표 노드 찾기
        preNode[v] 반환
        
for i in range(n+1) :
    preNode 자기 자신을 대표 노드로 초기화
    
for i in range(m) :
    연산 방식 cal과 대표 노드 start, 자식 노드 end 입력받기
    if cal == 0 :
        union 연산 수행
    else :
        집합에 속해있는지 아닌지 판단하는 변수 check 선언
        find(start) find(end) 수행 후, 두 대표 노드 비교
        if find(start) == find :
            True 반환
        if check :
            YES 출력하기
        else :
            NO 출력하기
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, m = map(int, input().split())

preNode = [0] * (n+1)

def union(a, b) :
    a = find(a)
    b = find(b)
    if a != b :
        preNode[b] = a

def find(v) :
    if preNode[v] == v :
        return v
    else :
        preNode[v] = find(preNode[v])
        return preNode[v]


for i in range(n+1) :
    preNode[i] = i
    
for i in range(m) :
    cal, parent, child = map(int, input().split())
    if cal == 0 :
        union(parent, child)
    else :
        check = False
        parentTmp = find(parent)
        childTmp = find(child)
        
        if parentTmp == childTmp :
            check = True
        
        if check :
            print("YES")
        else :
            print("NO")