'''5.빈 리스트에서 기존의 값들보다 큰 값이 추가될 때마다 카운팅
(값의 범위는 0~100이다.)
ex) 빈 리스트에서 [1, 3, 2, 6, 4, 9, 5]가 추가되는 상황
'''
# list_1 = []
# list_2 = [1, 3, 2, 6, 4, 9, 5]
# count = 1
# for i in range(len(list_2)):
#     list_1.append(list_2[i])
#     if(list_1[i] > list_1[i-1]):
#         count += 1
# print(list_1)
# print(count)

'''지우쌤'''
''''#방법1
arr = [1, 3, 2, 6, 4, 9, 5]
result = list()
count = 0
max = -1

#arr에 있는 모든 요소 x룰 순서대로 반복
for x in arr:
    # x값이 max값보다 크다면
    if x > max:
        #max값 x로 갱신
        max = x
        #count 1증가
        count += 1
print(count)'''

#방법2
arr = [1, 3, 2, 6, 4, 9, 5]
count = 1
max = arr[0]

#arr에 있는 일 [1]부터의 요소x를 순서대로 반복
for x in arr:
    # x값이 max값보다 크다면
    if x > max:
        #max값 x로 갱신
        max = x
        #count 1증가
        count += 1
print(count)