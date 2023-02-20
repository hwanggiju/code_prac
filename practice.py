# 더 맵게
from heapq import *
def solution(scoville, K):
    answer = 0
    h = []
    heapify(scoville)
    while True :
        try :
            if scoville[0] >= K:
                return answer
            
            a = heappop(scoville)
            
            new = a + (scoville[0] * 2)
            
            heappop(scoville)
            heappush(scoville, new)
            answer += 1
        except :
            return -1