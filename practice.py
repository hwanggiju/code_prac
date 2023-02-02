def solution(numbers):
    answer = [-1] * len(numbers)
    
    lst = []
    
    for i in range(len(numbers)) :
        tmp = numbers[i]
        
        while len(lst) > 0 :
            if numbers[lst[-1]] < tmp :
                idx = lst.pop()
                answer[idx] = tmp
            else :
                break
                
        lst.append(i)
        
    return answer