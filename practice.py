# 프로그래머스 - 연속된 부분 수열의 합

def solution(sequence, k):
    answer = []
    result = []
    
    startIdx = 0
    endIdx = 0
    
    n = len(sequence) - 1
    s = sequence[0]
    
    if k in sequence :
        idx = sequence.index(k)
        return [idx, idx]
    
    while endIdx < n :
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
            
    while startIdx < n :
        if s == k :
            result.append([startIdx, endIdx, endIdx-startIdx])
            break
            
        elif s > k :
            s -= sequence[startIdx]
            startIdx += 1
            
        else :
            break
            
    result.sort(key = lambda x : (x[2], x[0]))
    answer = result[0][:2]
    
    return answer