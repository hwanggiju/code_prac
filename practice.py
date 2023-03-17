# 백준 주몽의 명령

'''
재료의 개수 n과 갑옷이 되는 번호 m 입력 받기
재료 데이터 리스트에 저장하기 dataLst
dataLst 오름차순 정렬
시작점 인덱스 : startIndex = 0
끝점 인덱스 : endIndex = n-1
결과값 : count = 0

while i < j :
    if 재료합이 < M :
        시작점 1 증가
    elif 재료합이 > M :
        끝점 1 감소
    else :
        결과값 1 증가
        시작점 1 증가
        끝점 1 감소

결과값 출력
'''

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
        
dataLst = list(map(int, input().split(' ')))
dataLst.sort()

startIndex = 0
endIndex = n-1
count = 0

while startIndex < endIndex :
    if dataLst[startIndex] + dataLst[endIndex] < m :
        startIndex += 1
    elif dataLst[startIndex] + dataLst[endIndex] > m :
        endIndex -= 1
    else :
        count += 1
        startIndex += 1
        endIndex -= 1

print(count)