# 초콜릿 공장 문제 Solution

'''
cnt = 1
answer_list = ['다 먹었어요!']
while True :
    if cnt == 31 :
        print(answer_list[0])
        break
    
    print(f'초콜릿 {cnt}개 먹는중입니다.')
    cnt += 1
'''


# 돌발성 난청 진단 문제 Solution

n = int(input()) # 환자 수 입력
chart = [list(map(int, input().split())) for _ in range(n)] # 측정된 청력 역치 입력


for i in chart:
    idx_lst = []
    idx = 0
    for j in i :
        if j >= 30 :
            idx_lst.append(idx)
        idx += 1

    # queue를 이용하여 연속된 숫자 묶음 길이 계산
    tmp = []
    cnt = 0
    v = idx_lst.pop(0)
    tmp.append(v)

    while len(idx_lst) > 0 :
        v_cmp = idx_lst.pop(0)
        if v + 1 == v_cmp:
            cnt += 1
            tmp.append(v_cmp)
            v = v_cmp
        else :
            cnt = 0
            tmp = []
            tmp.append(v_cmp)
            v = v_cmp
        
    # 길이가 3보다 크면 진단
    # if len(tmp) >= 3 :
    if cnt >= 3 :
        print(f'돌발성 난청 진단')
        # break
    
    else :
        print('Fine!')


# 행렬 곱 문제 Solution

'''
A = int(input()) # 첫 번째 행렬의 행 개수 입력
arr_A = [list(map(int, input().split())) for _ in range(A)] # 첫번째 행렬 

B = int(input()) # 두 번째 행렬의 행 개수 입력
arr_B = [list(map(int, input().split())) for _ in range(B)] # 두번째 행렬

# print(arr_A, arr_B)

n = len(arr_A)
m = len(arr_B[0])

C = [[0]*m for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        for k in range(len(arr_A[0])) :
            C[i][j] += arr_A[i][k] * arr_B[k][j]
            
print(f'result = {C}')
'''