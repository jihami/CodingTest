# 2단계. 가장 많이 등장하는 수의 개수를 구합니다.
counter = [2, 3, 4, 5]

def 최대값(arr):
    large = 0
    for x in arr:
        if x > large:
                large = x
    return large
