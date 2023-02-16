# 폰켓몬 문제
def solution(nums):
    answer = 0
    
    a = len(set(nums))
    b = len(nums)/2
    
    if a >= b :
        answer = b
    else :
        answer = a
    
    return answer