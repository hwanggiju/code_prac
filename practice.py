# 백준 숫자 합 구하기

'''
n값 받기
공백 없는 숫자 입력값 받고, 리스트 자료구조로 저장하기
결과값 변수 sum 선언

for i in 리스트 :
    sum에 리스트 각 원소 정수로 변환하여 더하기

sum 출력
'''

n = input()
number = list(input())
sum = 0

for i in number :
    sum += int(i)
    
print(sum)