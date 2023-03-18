# 백준 카드 2

'''
카드 개수 n 입력받기
큐 리스트 생성하기 q

for i in range(1, n+1) :
    큐 리스트에 1부터 n까지 저장

while len(q) > 1 :
    맨 위의 카드 한 장을 버림
    그 다음 카드 한 장을 맨 뒤로 보냄
    
큐에서 마지막 하나 남은 원소 출력
'''

from collections import deque
n = int(input())

q = deque()

for i in range(1, n+1) :
    q.append(i)
    
while len(q) > 1 :
    q.popleft()
    q.append(q.popleft())
    
print(q[0])