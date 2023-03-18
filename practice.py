# 백준 수 정렬하기

'''
수의 개수 n 입력받기
숫자를 저장할 리스트 생성 dataLst
dataLst 입력받고 저장하기
오름차순 정렬
'''

n = int(input())

dataLst = []

for i in range(n) :
    val = int(input())
    dataLst.append(val)

dataLst.sort()

for i in range(n) :
    print(dataLst[i])