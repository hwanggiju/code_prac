import sys

input = sys.stdin.readline
result = ''
value = list(input())
value.remove('\n')
value.sort(key=int, reverse=True)
for i in value :
    result += i

print(result)
