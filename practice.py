# 백준 나머지 합 구하기

'''
수의 개수 n, 나누어떨어져야 하는 수 M 입력받기
Lst 리스트에 원본 리스트 저장
sumLst 리스트에 합 배열 저장
같은 나머지 인덱스 카운트 count 리스트 생성
정답 변수 answer 생성

for i in range(1, n+1) :
    합 배열 저장

for i in range(n) :
    합 배열 M으로 나머지 연산
    나머지가 0이라면 answer + 1
    나머지 값 인덱스 카운팅

for i in range(m) :
    count 리스트에서 2가지를 뽑는 경우의 수 answer에 더하기

answer 출력
'''

import sys

# 그냥 input()은 sys.stdin.readline 보다 개행 문자를 삭제해서 리턴하기 때문에 속도가 느리다.
# 반면 sys.stdin.readline는 개행 문자를 포함하여 출력하는 대신 속도가 빠른 편이다.
input = sys.stdin.readline
n, M = map(int, input().split())
Lst = list(map(int, input().split()))
sumLst = [0] * n
count = [0] * M
sumLst[0] = Lst[0]
answer = 0

for i in range(1, n) :
    sumLst[i] = sumLst[i-1] + Lst[i]
    
for i in range(n) :
    idx = sumLst[i] % M
    if idx == 0 :
        answer += 1
    count[idx] += 1
    
for i in range(M) :
    if count[i] > 1 :
        answer += (count[i] * (count[i] - 1)) // 2
        
print(answer)