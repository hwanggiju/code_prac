def plus(x, n) :
    return x + n
def double_(x) :
    return x * 2
def triple(x) :
    return x * 3

def solution(x, y, n):
    answer = 1
    nodeLst = []
    
    if x == y :
        return 0
    
    a = plus(x, n)
    b = double_(x)
    c = triple(x)
    
    if a < y :
        nodeLst.append(a)
    elif a == y :
        return answer
    
    if b < y :
        nodeLst.append(b)
    elif b == y :
        return answer
    
    if c < y :
        nodeLst.append(c)
    elif c == y :
        return answer
    
    while True :
        newnodeLst = []
        answer += 1
        
        for i in nodeLst :
            _plus = plus(i, n)
            _dou = double_(i)
            _tri = triple(i)
            
            if _plus < y :
                newnodeLst.append(_plus)
            elif _plus == y :
                return answer
            
            if _dou < y :
                newnodeLst.append(_dou)
            elif _dou == y :
                return answer
            
            if _tri < y :
                newnodeLst.append(_tri)
            elif _tri == y :
                return answer
            
        if len(newnodeLst) == 0 :
            return -1
        
        nodeLst = list(set(newnodeLst))
    
    return answer