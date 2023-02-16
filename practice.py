# 완주하지 못한 선수
def solution(participant, completion):
    answer = ''
    
    hash_table = {}
    
    for i in participant :
        if i not in hash_table :
            hash_table[i] = 1
            
        else :
            hash_table[i] += 1
    
    for i in completion :
        hash_table[i] -= 1
    
    for i in participant :
        if hash_table[i] == 1 :
            return i
    
    return answer