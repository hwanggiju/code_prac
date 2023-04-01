nowTemp, goalTemp = map(int, input().split())

cnt = 0
tmp = 0     # 몫
val = abs(nowTemp - goalTemp)

if val >= 10 :
    tmp = val // 10
val = val % 10
cnt += tmp

if val >= 8 :
    val -= 10
    val = abs(val) 
    cnt += 1

if val >= 5 :
    tmp = val // 5
    val = val % 5
    cnt += tmp

if val >= 3 :
    val -= 5
    val = abs(val)
    cnt += 1

if val >= 1 :
    tmp = val // 1
    cnt += tmp

    
print(cnt)
    