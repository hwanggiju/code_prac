# 백준 수 찾기 - 1920

'''
데이터 개수 n 입력받기
n개의 데이터 리스트 data 입력받고, 정렬하기

찾을 데이터 개수 findData 입력받기
찾을 데이터 리스트 findLst로 입력받고, 저장하기

for i in findLst :
    찾았는지 못찾았는지 find
    시작 인덱스 start와 끝 인덱스 end 초기화
    
    while start <= end :
        중앙값 m 값 대입
        if i < data[m] :
            end 값 중앙값 이전 인덱스로 업데이트
        elif i > data[m] :
            start 값 중앙값 다음 인덱스로 업데이트
        else :
            find 찾았다!!
            반복 종료
    if find :
        1 출력
    else :
        0 출력
'''

n = int(input())

data = list(map(int, input().split()))
data.sort()

findData = int(input())
findLst = list(map(int, input().split()))

for i in findLst :
    find = False
    start = 0
    end = len(data) - 1
    while  start <= end :
        m = (start + end) // 2
        if i < data[m] :
            end = m - 1
        elif i > data[m] :
            start = m + 1
        else :
            find = True
            break
    if find :
        print(1)
    else :
        print(0)
            
    