import sys

input = sys.stdin.readline

N = int(input())
pre = 0
post = 1
i = 0
def fun(i, pre, post):
    if N == 0 :
        return print(pre)
        
    if ((i%2) == 0) : 
        pre += post
        i += 1
    
    else :
        post += pre
        i += 1
        
    if (i == N) & (i%2 == 0) :
        return print(pre)
    
    elif (i == N) & (i%2 != 0) :
        return print(post)
    
    else :
        fun(i, pre, post)
        
fun(i, pre, post)