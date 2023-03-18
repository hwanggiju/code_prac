# 백준 DNA 비밀번호

'''
# 함수
add_(c) :
    새로운 값 더하고, check 업데이트
    
remove_(c) :
    맨 앞의 원소 제거하고, check 업데이트
    
# 메인 코드
문자열 크기 s와 부분 문자열 크기 p를 입력받기
DNA 문자열 데이터 arr 입력받기
A C G T 최소 개수 checkLst 입력받기

# 사용 변수 선언
결과값 변수 result = 0
비교 리스트 cmpLst
check = 0 

# 문제 해결 방법
for i in range(4) :
    checkLst에서 0인 원소 개수 만큼 check 값 증가 => 이유 : 최소 개수가 0이라는 것은 이미 만족되었다는 의미
    
for i in range(p) :
    부분 문자열 길이 원소 cmpLst와 checkLst를 비교하고, 유효한 원소라면 check 값 증가
    
if check == 4 :
    결과값 증가
    
for i in range(p, s) :
    tmpIdx = i - p
    add_(c) 새로운 원소 값 추가
    remove_(c) 맨 앞의 원소 값 제거
    if check == 4 :
        결과값 증가

결과값 출력
'''

def add_(c) :
    global checkLst, cmpLst, check
    if c == 'A' :
        cmpLst[0] += 1
        if cmpLst[0] == checkLst[0] :
            check += 1
    elif c == 'C' :
        cmpLst[1] += 1
        if cmpLst[1] == checkLst[1] :
            check += 1
    if c == 'G' :
        cmpLst[2] += 1
        if cmpLst[2] == checkLst[2] :
            check += 1
    if c == 'T' :
        cmpLst[3] += 1
        if cmpLst[3] == checkLst[3] :
            check += 1
    
def remove_(c) :
    global checkLst, cmpLst, check
    if c == 'A' :
        if cmpLst[0] == checkLst[0] :
            check -= 1
        cmpLst[0] -= 1
    elif c == 'C' :
        if cmpLst[1] == checkLst[1] :
            check -= 1
        cmpLst[1] -= 1
    elif c == 'G' :
        if cmpLst[2] == checkLst[2] :
            check -= 1
        cmpLst[2] -= 1
    elif c == 'T' :
        if cmpLst[3] == checkLst[3] :
            check -= 1
        cmpLst[3] -= 1
        

s, p = map(int, input().split())
arr = list(input())
checkLst = list(map(int, input().split()))

result = 0
cmpLst = [0] * 4
check = 0

for i in range(4) :
    if checkLst[i] == 0 :
        check += 1

for i in range(p) :
    add_(arr[i])
    
if check == 4 :
    result += 1
    
for i in range(p, s) :
    tmpIdx = i - p
    add_(arr[i])
    remove_(arr[tmpIdx])
    if check == 4 :
        result += 1
        
print(result)