# 백준 버블 소트2

'''
병합 정렬 구현
def merge_sort(시작 인덱스 s, 끝 인덱스 e) :
    if e - s < 1 :
        종료
    중간점 설정
    merge_sort(s, m) 재귀 함수로 집합 분할하기
    merge_sort(m, e) 재귀 함수로 집합 분할하기
    for i in range(s, e+1) :
        임시 리스트 tmp에 원본 리스트 값 저장
    tmp 정렬 삽입 인덱스 k
    앞쪽 그룹 시작 인덱스 idx1
    뒤쪽 그룹 시작 인덱스 idx2
    while idx1 <= m and idx2 <= e :
        양쪽 그룹 index가 가리키는 값 비교 후 더 작은 수를 선택해 리스트에 저장하기
        선택된 데이터 index 오른쪽으로 한칸 이동
        반복문이 끝난 후 남은 데이터 정리
        뒤쪽에 있는 데이터가 더 작아 선택될 때, swap이 일어난 것과 같기 때문에, 앞에 있는 데이터 개수만큼 결과값에 더하기
        
수의 개수 n
정렬 리스트 arr에 입력받고 저장하기
정렬할 때 사용할 임시 리스트 생성하기 tmp
병합 정렬 함수 수행하기
결과값 출력
'''
import sys

input = sys.stdin.readline

result = 0

def merge_sort(s, e) :
    global result
    if e - s < 1 :
        return
    m = int(s + (e-s) / 2)
    merge_sort(s, m)
    merge_sort(m+1, e)
    
    for i in range(s, e+1) :
        tmp[i] = arr[i]
        
    k = s
    idx1 = s
    idx2 = m+1
    
    while idx1 <= m and idx2 <= e :
        if tmp[idx1] > tmp[idx2] :
            arr[k] = tmp[idx2]
            result = result + idx2 - k  # swap 횟수 결과값 저장
            k += 1
            idx2 += 1
        else :
            arr[k] = tmp[idx1]
            k += 1
            idx1 += 1
        
    while idx1 <= m :
        arr[k] = tmp[idx1]
        k += 1
        idx1 += 1
        
    while idx2 <= e :
        arr[k] = tmp[idx2]
        k += 1
        idx2 += 1
        
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
tmp = [0] * (n + 1)
merge_sort(1, n)
print(result)