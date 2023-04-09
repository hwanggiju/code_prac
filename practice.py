# 프로그래머스 - 달리기 경주

def change(players, idx) :
    tmp = players[idx]
    players[idx] = players[idx-1]
    players[idx-1] = tmp
    return players

def solution(players, callings):
    answer = []
    dic = {}
    for i in range(len(players)) :
        dic[players[i]] = i
        
    for j in callings :
        idx = dic[j]
        tmp = players[idx-1]
        dic[j] -= 1
        dic[tmp] += 1
        players = change(players, idx)
    result = sorted(dic.items(), key = lambda x : x[1])
    for name, _ in result :
        answer.append(name)
    return answer