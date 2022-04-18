import sys

input = sys.stdin.readline
index = int(input())
value = []

for i in range(index) :
    value.append(int(input()))
    
value.sort()

for j in value :
    print(j)