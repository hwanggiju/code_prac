from heapq import *
def solution(book_time):
    answer = 0
    
    timeLst = []
    heapLst = []
    
    for i in book_time :
        startTime, endTime = i
        startLst = startTime.split(":")
        endLst = endTime.split(":")
        s_hour = int(startLst[0]) * 60
        s_minute = int(startLst[1])
        e_hour = int(endLst[0]) * 60
        e_minute = int(endLst[1])
        timeLst.append([s_hour + s_minute, e_hour + e_minute + 10])
        
    timeLst = sorted(timeLst, key = lambda x:x[0])
    
    for i in timeLst :
        tmp = i[0]
        if len(heapLst) == 0 :
            heappush(heapLst, i[1])
        
        elif heapLst and tmp >= heapLst[0] :
            heappushpop(heapLst, i[1])
            
        else :
            heappush(heapLst, i[1])
    
    answer = len(heapLst)
    
    return answer