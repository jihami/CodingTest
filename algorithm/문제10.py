# ex) [3,6,2,7]
# 값의 범위:  0 ~ 10 양 끝 모두 포함
# arr의 길이 : 1개 이상

arr = [3,6,2,7]
result = arr[0]
# 처음에 arr[0]와 arr[0]가 비교되므로 비효율적
for x in arr:
    # result: 기존값, x: 새로 들어오는 값
    if result < x:
        result = x

print(result)