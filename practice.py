# 최소 직사각형
def solution(sizes):
    answer = 0
    w = []
    h = []
    
    for x, y in sizes :
        if x > y :
            w.append(x)
            h.append(y)
        else :
            w.append(y)
            h.append(x)
    a = max(w)
    b = max(h)
    
    answer = a*b
            
    return answer