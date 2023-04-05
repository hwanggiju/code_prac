# 프로그래머스 - 공원 산책

def solution(park, routes):
    answer = []
    cord = [0, 0]
    for i in range(len(park)) :
        for j in range(len(park[0])) :
            if park[i][j] == 'S' :
                cord = [i, j]
                break
            
    for i in routes :
        order, move = i.split(' ')
        move = int(move)
        x, y = cord
        print('base', cord)
        for j in range(1, move+1) :
            if order == 'E' :
                # 오른쪽 이동
                if y+move >= len(park[0]) or park[x][y+j] == 'X' :
                    cord = [x,y]
                    break
                else :
                    cord = [x, y+j]
            elif order == 'W' :
                # 왼쪽 이동
                if y-move < 0 or park[x][y-j] == 'X' :
                    cord = [x,y]
                    break
                else :
                    cord = [x, y-j]
                    
            elif order == 'S' :
                # 아래 이동
                if x+move >= len(park) or park[x+j][y] == 'X' :
                    cord = [x,y]
                    break
                else :
                    cord = [x+j, y]
                    
            elif order == 'N' :
                # 위로 이동
                if x-move < 0 or park[x-j][y] == 'X' :
                    cord = [x,y]
                    break
                else :
                    cord = [x-j, y]
            print(cord)
    
    
    return cord