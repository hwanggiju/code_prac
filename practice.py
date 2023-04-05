# 프로그래머스 - 과제 진행하기
def solution(plans):
    result = []
    stop = []
    for i in range(len(plans)) :
        subject, startTime, play = plans[i]
        tmpLst = startTime.split(':')
        plans[i][1] = int(tmpLst[0]) * 60 + int(tmpLst[1])
        plans[i][2] = int(play)
        
    plans.sort(key = lambda x : x[1])
    
    for i in range(len(plans)) :
        subject, startTime, play = plans[i]
        endTime = startTime + play
        if i == len(plans) - 1 :
            result.append(subject)
        
        elif i+1 < len(plans) and endTime <= plans[i+1][1] :
            result.append(subject)
            remain = plans[i+1][1] - endTime
            
            while remain > 0 and len(stop) > 0:
                tmpSub, tmpTime = stop.pop()
                
                if tmpTime <= remain :
                    result.append(tmpSub)
                    remain -= tmpTime

                else :
                    stop.append([tmpSub, tmpTime - remain])
                    break
        
        else :
            stop.append([subject, endTime - plans[i+1][1]])
    
    while len(stop) > 0 :
        s, _ = stop.pop()
        result.append(s)
    
    return result