n = int(input()) # 토핑의 종류 수
a, b = map(int, input().split()) # 도우의 가격, 토핑의 가격
c = int(input()) # 도우의 칼로리
n_cal = [] # 토핑 칼로리 리스트
result_cal = [] # 최고의 피자 리스트
for _ in range(n) :
    cal = int(input())
    n_cal.append(cal)

n_cal.sort(reverse=True)

money = a
result = c

for i in range(n) :
    money += b
    result += n_cal[i]
    result_cal.append((result // money))
    
print(max(result_cal))