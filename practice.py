# 기능개발
import math
def solution(progresses, speeds):
    answer = []
    dayLst = []
    q = []
    
    for i, j in zip(progresses, speeds) :
        tmp = 100 - i
        day = math.ceil(tmp / j)
        dayLst.append(day)
    
    q.append(dayLst[0])
    
    for i in range(1, len(dayLst)) :
        if q[0] >= dayLst[i] :
            q.append(dayLst[i])
        elif q[0] < dayLst[i] :
            answer.append(len(q))
            q = []
            q.append(dayLst[i])
        
        if i == (len(dayLst) - 1) :
            answer.append(len(q))
            
    return answer