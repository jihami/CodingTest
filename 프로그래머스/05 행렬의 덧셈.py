import copy

def solution(arr1,arr2):
    행길이 = len(arr1)
    열길이 = len(arr2)
    answer = [0]*열길이
    answer = [copy.deepcopy(answer) for _ in range(행길이)]
    for i in range(행길이):
        for j in range(열길이):
            answer[i][j]=arr1[i][j]+arr2[i][j]
    return  answer


# def solution(arr1, arr2):
#     answer = []
#
#     for i in range(len(arr1)):
#         arr_sum = []
#         for j in range(len(arr1[0])):
#             arr_sum.append(arr1[i][j] + arr2[i][j])
#         answer.append(arr_sum)
#
    # return answer