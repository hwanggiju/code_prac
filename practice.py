def solution(cap, n, deliveries, pickups):
    answer = 0
    
    idx = n - 1
    
    d_p = [0, 0]
    
    while idx >= 0 :
    	
        d_p[0] += deliveries[idx]
        d_p[1] += pickups[idx]
        
        while d_p[0] > 0 or d_p[1] > 0 :
            d_p[0] -= cap
            d_p[1] -= cap
            answer += (idx + 1) * 2
        
        idx -= 1
        
    return answer