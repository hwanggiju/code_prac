# 백준 수 정렬하기

'''
배열의 크기 n 입력받기

for i in range(n) :
    arr 리스트에 데이터와 인덱스 저장
    
최댓값 저장 변수 max_ 생성
arr 정렬

for i in range(n) :
    if max_ < arr[i][1] - i :
        최댓값 업데이트
        
최댓값 + 1 출력
'''

import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n) :
    arr.append((int(input()), i))
    
max_ = 0
arr.sort()

for i in range(n) :
    if max_ < arr[i][1] - i :
        max_ = arr[i][1] - i
        
print(max_ + 1)