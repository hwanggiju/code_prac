pasta = []
juice = []

for i in range(5) :
    val = int(input())
    if i < 3:
        pasta.append(val)
    else :
        juice.append(val)

result = []
for p in pasta :
    for j in juice :
        tmp = (p+j) + (p + j) * 0.1
        result.append(tmp)
        
print(min(result))
        
    