def solution(storey):
    answer = 0
    while storey :
        b = storey % 10
        n = (storey // 10) % 10
        
        if b > 5 :
            answer += 10 - b
            storey += 10  
        elif b == 5 :
            answer += b
            if n >= 5 :
                storey += 10
        else :
            answer += b
            
        storey = storey // 10
    return answer