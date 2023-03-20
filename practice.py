# 백준 신기한 소수

'''
자릿수 n 입력받기

def 소수 판별 함수() :
    for i in range(2, int(val / 2 + 1)) :
        if val 나누기 i == 0 :
            return False
        return True
    
def DFS(현재 수) :
    if 자릿수 == n :
        현재 수 출력
    else :
        for i in range(1, 10) :
            if (i 나누기 2 != 0) and ( 현재수 * 10 + i == 소수 ) :
                DFS(현재수 * 10 + i) .
2, 4, 5, 7 DFS 수행
'''

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())

def isPrime(val) :
    for i in range(2, int(val /2 + 1)) :
        if val % i == 0 :
            return False
    return True

def DFS(num) :
    if len(str(num)) == n :
        print(num)
        
    for i in range(1, 10) :
        if ((i % 2 != 0) and (isPrime(num * 10 + i))) :
            DFS(num * 10 + i)
            
DFS(2)
DFS(3)
DFS(5)
DFS(7)