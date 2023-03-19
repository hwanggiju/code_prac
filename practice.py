# 백준 수 정렬하기 3

'''
수의 개수 n 입력받기
카운팅 정렬 리스트 생성하기 countLst

for i in range(n) :
    입력받은 값을 인덱스로 countLst에 1 증가
    
for i in range(10001) :
    if countLst[i] != 0 :
        countLst[i]만큼 인덱스 출력
'''

import sys

input = sys.stdin.readline

n = int(input())
countLst = [0] * 10001

for i in range(n) :
    countLst[int(input())] += 1
    
for i in range(len(countLst)) :
    if countLst[i] != 0 :
        for j in range(countLst[i]) :
            print(i)
