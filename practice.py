# 백준 평균 구하기

'''
n 과목 수 입력받기
score 리스트에 입력받은 점수 정보 저장하기
max_ 변수에 점수 최대값 저장하기
score 리스트 점수 총합 구하기
평균값 계산식으로 출력하기
'''

n = int(input())
score = list(map(int, input().split()))
max_ = max(score)
sum_ = sum(score)
print(sum_*100/max_/n)