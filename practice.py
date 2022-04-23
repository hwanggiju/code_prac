import sys

input = sys.stdin.readline

N = int(input())
lst = input().split(' ')
dic = {}
lst[N-1] = lst[N-1].rstrip('\n')
cnt = []

for i in range(N) :
    lst[i] = int(lst[i])
    
lst_new = sorted(list(set(lst)))

for i in range(len(lst_new)) :
    dic[lst_new[i]] = i
    
for i in lst:
    cnt.append(dic[i])
    
print(*cnt)
