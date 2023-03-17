# 백준 '좋은 수' 구하기

'''
수의 개수 n 입력받기
n개의 데이터를 리스트에 저장 dataLst
dataLst 오름차순으로 정렬
결과값 변수 count = 0

for i in range(n) :
    기준이 되는 값 dataLst[i]
    시작점 : startIndex = 0
    끝점 : endIndex = n-1
      
    while startIndex < endIndex :
        if dataLst[startIndex] + dataLst[endIndex] == 기준값 :
            if 시작점 != 기준값 and 끝점 != 기준값 :
                결과값 1 증가
                 break
            if 시작점 == 기준값 :
                시작점 인덱스 1 증가
            if 끝점 == 기준값 :
                끝점 인덱스 1 감소
        elif dataLst[startIndex] + dataLst[endIndex] > 기준값 :
            끝점 인덱스 1 감소
        else : 
            시작점 인덱스 1 증가

결과값 출력
'''

import sys
input = sys.stdin.readline

n = int(input())
        
dataLst = list(map(int, input().split(' ')))
dataLst.sort()

count = 0

for i in range(n) :
    val = dataLst[i]
    startIndex = 0
    endIndex = n-1
    while startIndex < endIndex :
        if dataLst[startIndex] + dataLst[endIndex] == val :
            if dataLst[startIndex] != val and dataLst[endIndex] != val :
                count += 1
                break
            if dataLst[startIndex] == val :
                startIndex += 1
            if dataLst[endIndex] == val :
                endIndex -= 1
        elif dataLst[startIndex] + dataLst[endIndex] > val :
            endIndex -= 1
        else : startIndex += 1
        
print(count)