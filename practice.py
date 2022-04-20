import sys
from collections import Counter


input = sys.stdin.readline

num = int(input())
value = []

for i in range(num):
    value.append(int(input()))

value.sort()   
 
# ---------------------------------------------
aver = 0
for i in value:
    aver += i
aver /= num

# ---------------------------------------------
index = int(num / 2)
medi = value[index]

# ---------------------------------------------
c = Counter(value)
val = c.most_common()
maximum = val[0][1]
mode = []

for i in val:
    if i[1] == maximum:
        mode.append(i[0])
    else :
        mode.append(val[0][0])
        
# ---------------------------------------------
M, m = max(value), min(value)

print(round(aver))
print(medi)
if len(mode) > 1 :
    print(mode[1])
else :
    print(mode[0])
print(M-m)