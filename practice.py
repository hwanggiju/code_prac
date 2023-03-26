# 백준 소수 구하기 1929

'''
m이상 n이하의 m, n 입력받기
소수 탐색 리스트 primeLst 초기화하기

for i in range(2, n+1) :
    primeLst에 순서대로 데이터 업데이트

for i in range(2, int(math.sqrt(n)) + 1) : # 2부터 제곱근 n 이하까지 탐색하기
    if primeLst[i] == 0 :
        continue
    for j in range(i+i, n+1, i) :
        primeLst[i] 배수 삭제하기

for i in range(m, n+1) :
    primeLst[i] 남은 소수 차례대로 출력하기
'''

import math

m, n = map(int, input().split())
primeLst = [0] * (n+1)

for i in range(2, n+1) :
    primeLst[i] = i

for i in range(2, int(math.sqrt(n)) + 1) :
    if primeLst[i] == 0 :
        continue
    for j in range(i+i, n+1, i) :
        primeLst[j] = 0

for i in range(m, n+1) :  
    if primeLst[i] != 0 :
        print(primeLst[i])