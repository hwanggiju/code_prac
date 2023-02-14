import sys

sys.setrecursionlimit(10000)

def bfs(maps, x, y, s) :
    
    if x >= len(maps[0]) or y >= len(maps) or x < 0 or y < 0 :
        return s
    
    if maps[y][x] == "X" :
        return s
    
    s += int(maps[y][x])
    
    maps[y][x] = "X"
    
    s = bfs(maps, x, y - 1, s)  # 상
    s = bfs(maps, x, y + 1, s)  # 하
    s = bfs(maps, x - 1, y, s)  # 좌
    s = bfs(maps, x + 1, y, s)  # 우

    return int(s)

def solution(maps):
    answer = []
    map_ = []

    for i in maps :  
        map_.append(list(i))

    for i in range(len(map_)) :
        for j in range(len(map_[0])) :
            if map_[i][j] == "X" :
                pass
            else :
                answer.append(bfs(map_, j, i, 0))

    if answer :
        answer = sorted(answer)
    else :
        answer.append(-1)
    
    return answer