# 백준 오큰수

'''
수열 개수 n, 수열 리스트 dataLst 입력받기
result 오큰수 결과 리스트 생성
stack 인덱스 저장 리스트 생성

for i in range(n) :
    while stack and dataLst[stack[-1]] < dataLst[i] :
        stack top 인덱스 pop idx 저장
        result[idx] dataLst[i] 추가
        
    stack에 i 인덱스 추가
    
while stack :
    stack 비어있을 때까지 pop, idx에 저장
    남아있는 인덱스 오큰수가 없는 경우이므로, result[idx] = -1
    
for i in range(n) :
    결과값 띄어쓰기로 출력하기
'''

n = int(input())
dataLst = list(map(int, input().split()))

result = [0] * n
stack = []

for i in range(n) :
    while stack and dataLst[stack[-1]] < dataLst[i] :
        idx = stack.pop()
        result[idx] = dataLst[i]
    stack.append(i)
    
while stack :
    idx = stack.pop()
    result[idx] = -1

for i in range(n) :
    print(str(result[i]) + ' ', end='')