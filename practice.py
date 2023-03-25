# 백준 잃어버린 괄호 - 1541

'''
정답 변수 answer 초기화
입력받은 계산식 '-' 문자로 쪼개서 리스트로 저장하기

for i in range(len(cal)) :
    더하기 결과값 변수 result 초기화
    '+' 문자로 쪼개서 tmp 리스트로 저장하기
    for j in tmp :
        result에 int(j) 누적하기
    
    if i == 0 :
        가장 첫번째 숫자는 answer 그냥 더해주기
    else :
        나머지 숫자는 answer에 result 만큼 빼기

answer 출력하기
'''

answer = 0
cal = input().split('-')

for i in range(len(cal)) :
    result = 0
    tmp = cal[i].split('+')
    for j in tmp :
        result += int(j)
    if i == 0 :
        answer += result
    else : 
        answer -= result

print(answer)