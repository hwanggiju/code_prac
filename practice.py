H, M = map(int, input().split(' '))

T = (H * 60) + M
H_M = T - 45

if H_M > 0 :
    H = int(H_M / 60)
    M = int(H_M % 60)
    print(H, M)
    
elif H_M < 0 :
    H_M = 1440 + H_M
    H = int(H_M / 60)
    M = int(H_M % 60)
    print(H, M)

else :
    H = int(H_M / 60)
    M = int(H_M % 60)
    print(H, M)