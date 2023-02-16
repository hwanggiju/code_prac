# 위장
def solution(clothes):
    answer = 1
    h = {}
    for _, x in clothes :
        if x not in h :
            h[x] = 2
        else :
            h[x] += 1
            
    for i in h.values():
        answer *= i
    return answer - 1