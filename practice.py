# 백준 ATM

'''
사람 수 n 입력받기
인출 시간 p 입력받고 리스트에 저장하기
합 배열 sumLst 생성하기

인출 시간 리스트 오름차순으로 정렬하기

정렬된 데이터 합 배열 생성하기 sumLst

합 배열의 모든 값을 더해 결과값 출력
'''

n = int(input())
p = list(map(int, input().split()))
sumLst = [0] * n

p.sort()
sumLst[0] = p[0]

for i in range(1, n) :
    sumLst[i] = sumLst[i-1] + p[i]

result = sum(sumLst)

print(result)