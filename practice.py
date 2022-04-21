import sys

input = sys.stdin.readline
num = int(input())
value = []

for i in range(num):
    x, y = map(int, input().split(' '))
    tup = (x, y)
    value.append(tup)
    
value.sort()

for i in value :
    print(i[0], i[1])
print(value)