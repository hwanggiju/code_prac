def solution(data, col, row_begin, row_end):
    answer = 0
    tmp = 0
    data = sorted(data, key = lambda x : (x[col-1], -x[0]))
    # print(data)
    data = data[row_begin-1 : row_end]
    # print(data)
    
    for i in data :
        sum = 0
        
        for j in i :
            sum += j % row_begin
            
        if tmp == 0 :
            tmp = sum
        else :
            tmp = tmp ^ sum
        
        row_begin += 1    
    
    # print(tmp)
    answer = tmp
    
    return answer