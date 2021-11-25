'''7.리스트에서 특정 원소만 추출하기
ex)  [1, 2, 2, 2, 3, 1, 1, 3, 2] 에서  2를 제외한 나머지만 추출하기
'''
arr = [1, 2, 2, 2, 3, 1, 1, 3, 2]
# # 방법 1 - remove 비추 쓰지 않는걸로!!
# # arr의 반복횟수를 구한다.
# 반복횟수=arr.count(2)
#
# # 반복횟수 만큼
# for i in range(반복횟수):
#    # 2를 지운다
#    arr.remove(2)
# print(arr)
# 방법 2
result = list()
for x in arr:
    if x != 2:
        #result에 x추가
        result.append(x)
print(result)
