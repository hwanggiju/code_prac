# 프로그래머스 - 추억의 점수

def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)) :
        dic[name[i]] = yearning[i]
    for na in photo :
        s = 0
        for j in range(len(na)) :
            if na[j] not in dic :
                pass
            else :
                s += dic[na[j]]
        answer.append(s)
    return answer