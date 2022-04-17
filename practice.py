A, B, C = map(int, input().split(' '))

if (A == B) &  (A == C) :
    reward = 10000 + (A * 1000)
    print(reward)
    
elif (A == B) & (A != C):
    reward = 1000 + (A * 100)
    print(reward)

elif (B == C) & (A != C) :
    reward = 1000 + (B * 100)
    print(reward)
    
elif (A == C) & (B != C) :
    reward = 1000 + (A * 100)
    print(reward)
    
else :
    if (A > B) & (A > C) :
        print(A * 100)
        
    elif (B > A) & (B > C) :
        print(B * 100)
        
    else :
        print(C * 100)