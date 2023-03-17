# 백준 연속된 자연수의 합 구하기

'''
n 입력받기
사용 변수 선언 (결과값 count, 시작점 startIndex, 끝점 endIndex, 합산 sum_)

while endIndex != n :
    if sum_ == n :
        결과값 1 증가시키기
        끝점 1 증가시키기
        끝점 합산에 누적하기
    elif sum_ > n :
        시작점 합산에서 빼주기
        시작점 1 증가시키기
    else :
        끝점 1 증가시키기
        끝점 합산에 누적하기

결과 값 출력
'''

n = int(input())

count = 1
startIndex = 1
endIndex = 1
sum_ = 1

while endIndex != n :
    if sum_ == n :
        count += 1
        endIndex += 1
        sum_ += endIndex
        
    elif sum_ > n :
        sum_ -= startIndex
        startIndex += 1
        
    else :
        endIndex += 1
        sum_ += endIndex
        
print(count)
        
        