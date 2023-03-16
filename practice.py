# 빅-오메가 표기법 시간 복잡도 = 1 번
# 빅-세타 표기법 시간 복잡도 = N/2 번
# 빅-오 표기법 시간 복잡도 = N 번
import random
findNumber = random.randrange(1, 101)   # 1~100 사이 랜덤값 생성

for i in range(1, 101) :
    if i == findNumber :
        print(i)
        break