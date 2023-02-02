from heapq import *
def solution(numbers):
    answer = [-1] * len(numbers)
    
    lst = []
    
    for i in range(len(numbers)) :
        tmp = numbers[i]
        
        while True :
            if len(lst) > 0 and lst[0][0] < tmp :
                val, idx = heappop(lst)
                answer[idx] = tmp
            else :
                break
                
        heappush(lst, [tmp, i])
        
    return answer