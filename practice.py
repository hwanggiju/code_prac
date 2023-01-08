from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    d_lst = deque()
    p_lst = deque()
    
    d_idx = len(deliveries) - 1
    p_idx = len(pickups) - 1 
    
    tmp = [0, 0]
    d_box = 0
    p_box = 0
    while d_idx > -1 :
        
        d_box = tmp[0] + deliveries[d_idx] - cap
            
        if (tmp[0] == 0) and (deliveries[d_idx] > 0) :
            d_lst.append(d_idx)
            
        if d_box <= 0 :
            tmp[0] += deliveries[d_idx]
            deliveries[d_idx] = 0
            
        elif d_box > 0 :
            deliveries[d_idx] -= cap - tmp[0]
            tmp[0] = 0
            continue
            
        d_idx -= 1
    
    while p_idx > -1 :
        
        p_box = tmp[1] + pickups[p_idx] - cap
            
        if (tmp[1] == 0) and (pickups[p_idx] > 0) :
            p_lst.append(p_idx)
            
        if p_box <= 0 :
            tmp[1] += pickups[p_idx]
            deliveries[p_idx] = 0
            
        elif p_box > 0 :
            pickups[p_idx] -= cap - tmp[1]
            tmp[1] = 0
            continue
            
        p_idx -= 1
        
    
    if len(d_lst) > 0 and len(p_lst) > 0:
        min_len = len(d_lst) if len(d_lst) < len(p_lst) else len(p_lst)
        for _ in range(min_len):
            d_last = d_lst.popleft()
            p_last = p_lst.popleft()
            answer += 2 * (p_last + 1 if p_last > d_last else d_last + 1)
        while len(d_lst) > 0:
            answer += 2 * (d_lst.popleft() + 1)
        while len(p_lst) > 0:
            answer += 2 * (p_lst.popleft() + 1)
    # for i, j in zip(d_lst, p_lst) :
    #     answer += max(i * 2, j * 2)
        
    return answer
