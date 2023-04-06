def solution(sequence, k):
    answer = []
    result = []
    
    startIdx = 0
    endIdx = 0
    
    n = len(sequence)-1
    s = sequence[0]
    
    if k in sequence :
        idx = sequence.index(k)
        return [idx, idx]
    
    while endIdx != n :
        if s == k :
            result.append([startIdx, endIdx, endIdx-startIdx])
            endIdx += 1
            s += sequence[endIdx]
            
        elif s > k :
            s -= sequence[startIdx]
            startIdx += 1
            
        else :
            endIdx += 1
            s += sequence[endIdx]
            
        # print(startIdx, endIdx)
            
        if endIdx == n and s > k:
            while s >= k :
                if s == k :
                    result.append([startIdx, endIdx, endIdx-startIdx])
                    break
                else :
                    s -= sequence[startIdx]
                    startIdx += 1
                # print('part',startIdx, endIdx)
            break
    # print(result)
    result.sort(key = lambda x : (x[2], x[0]))
    answer = result[0][:2]
    
    return answer