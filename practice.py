# 백준 구간 합 구하기 4

'''
수의 개수 n과 합을 구해야 하는 횟수 M 입력받기
numLst 에 n개의 수 리스트에 저장
sumArray 합 배열 선언
temp 변수 선언

for i in numLst :
    temp 에 i 숫자 더하기
    합 배열에 추가하기

for i in range(M) ;
    구간 합 적용해서 출력하기
'''

import sys

# 그냥 input()은 sys.stdin.readline 보다 개행 문자를 삭제해서 리턴하기 때문에 속도가 느리다.
# 반면 sys.stdin.readline는 개행 문자를 포함하여 출력하는 대신 속도가 빠른 편이다.
input = sys.stdin.readline
n, M = map(int, input().split())
numLst = list(map(int, input().split()))
sumArray = [0]
temp = 0

for i in numLst :
    temp += i
    sumArray.append(temp)
    
for i in range(M) :
    start, end = map(int, input().split())
    print(sumArray[end] - sumArray[start-1])