# 백준 스택 수열

'''
수열의 개수 n과 수열 리스트 arr 데이터 입력받기
오름차순 자연수 num = 0
stack 리스트 생성
결과값 result 빈 문자열 생성
정상적인 수열 확인 state = True

for i in range(n) :
    val arr[i] 수열 데이터 저장
    if val >= num :
        while val >= num :
            num을 stack에 추가
            num 1 증가
            result + 추가
        마지막 원소 제거
        result - 추가
    else :
        stack 마지막 원소 pop 후 temp에 저장
        if temp != val :
            print("NO")
            state = False
            break
        else :
            result - 추가

if state :
    결과값 출력
'''

n = int(input())
arr = [0] * n

for i in range(n) :
    arr[i] = int(input())
    
stack = []
result = ""
state = True
num = 1

for i in range(n) :
    val = arr[i]
    if val >= num :
        while val >= num :
            stack.append(num)
            num += 1
            result += '+\n'
        stack.pop()
        result += '-\n'
        
    else :
        temp = stack.pop()
        if temp != val :
            print("NO")
            state = False
            break
        else :
            result += '-\n'

if state :
    print(result)