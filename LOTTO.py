import random
from itertools import combinations

LOTTO = range(1, 46)

for _ in range(5) :
    temp = random.sample(LOTTO, 6)
    print(temp)