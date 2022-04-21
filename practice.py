import sys

input = sys.stdin.readline
num = int(input())
value = []

for i in range(num):
    x, y = map(int, input().split(' '))
    x_y_list = [x, y]
    value.append(x_y_list)
    
for i in value :
    temp_1 = i[0]
    i[0] = i[1]
    i[1] = temp_1
    
value.sort()

for i in value :
    temp_2 = i[0]
    i[0] = i[1]
    i[1] = temp_2

for i in value :
    print(i[0], i[1])