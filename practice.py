import sys

input = sys.stdin.readline
index = int(input())
cnt = [0 for x in range(10001)]

for _ in range(index) :
    cnt[int(input())] += 1
    
for i in range(1, 10001) :
    for j in range(cnt[i]) :
        print(i)