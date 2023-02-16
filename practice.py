# 전화번호 목록
from collections import Counter

def solution(phone_book):
    answer = True
    
    hash_t = Counter(phone_book)
        
    for i in phone_book :
        tmp = ''
        for j in i :
            tmp += j
            if tmp in hash_t and tmp != i :
                return False
    return answer