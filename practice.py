A, B = map(int, input().split(' '))
C = int(input())

T = (A * 60) + B
A_B = T + C

if A_B >= 1440 :
    A_B = A_B - 1440
    A = int(A_B / 60)
    B = int(A_B % 60)
    print(A, B)

elif A_B > 0 :
    A = int(A_B / 60)
    B = int(A_B % 60)
    print(A, B)
    
else :
    A = int(A_B / 60)
    B = int(A_B % 60)
    print(A, B) 