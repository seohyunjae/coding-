#떡의 개수와 떡의 길이 받기
n, m = list(map(int, input().split(' ')))
#각 떡의 개별 높이 정보 입력
array = list(map(int,input().split()))
#이진 탐색을 위한 시작점 끝점
start = 0
end = max(array)

#이진 탐색(반복)
result = 0
while(start < end):
    total = 0 #떡의 총합
    mid = (start+end)//2 #중간값
    for x in array:
        if x > mid:#각각의 값이 중간값보다 클때
            total += x - mid
                
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid+1


print(result)
