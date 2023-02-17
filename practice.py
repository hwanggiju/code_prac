# 같은 숫자는 싫어
def solution(arr):
    answer = []
    
    for i in arr :
        if len(answer) == 0 :
            answer.append(i)
            
        elif len(answer) != 0 and answer[-1] != i :
            answer.append(i)
            
    return answer