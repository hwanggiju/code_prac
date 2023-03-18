# 백준 절대값 힙

'''
연산 개수 n 입력받기
우선순위 큐 리스트 생성 pq

for i in range(n) :
    정수 입력 받기 val
    if val == 0 :
        if pq.empty() :
            0 출력하기
        else :
            pq의 맨 앞의 원소 출력하기 (get())
            
    else :
        pq의 새로운 기준으로 정렬하기 (put())
'''

from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
pq = PriorityQueue()

for i in range(n) :
    val = int(input())
    if val == 0 :
        if pq.empty() :
            print('0\n')
        else :
            temp = pq.get()
            print(str(temp[1]) + '\n')
    else :
        # abs(val) 기준으로 먼저 정렬
        # abs(val)이 같다면, val를 기준으로 정렬하여 양수 음수 판별 
        pq.put((abs(val), val))
