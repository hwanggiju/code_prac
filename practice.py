import sys

input = sys.stdin.readline

person = int(input())
lst = [0 for _ in range(person)]

for i in range(person) :
    age, name = map(str, input().split(' '))
    lst[i] = [int(age), name]
    lst[i][1] = lst[i][1].rstrip('\n')
    
lst = sorted(lst, key = lambda x : x[0])

for i in lst :
    print(i[0], i[1])    