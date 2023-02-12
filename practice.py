def solution(s, skip, index):
    answer = ''
    for i in range(len(s)) :
        cnt = 0
        atoz = ord(s[i]) - ord('a')
        
        while (cnt < index) :
            
            atoz += 1
            tmp = chr((atoz % 26) + ord('a'))
            
            if tmp not in skip :
                cnt += 1
                
        answer += tmp

    return answer