from heapq import heappushpop, heappush
def solution(n, k, enemy):
    answer = 0
    lst = []
    s = 0
    for i in enemy :
        s += i
        if s <= n :
            heappush(lst, -i)
            answer += 1
        elif k > 0 :
            k -= 1
            s += heappushpop(lst, -i)
            answer += 1
        else :
            break 
            
    return answer
