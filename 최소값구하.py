# 2단계. 가장 많이 등장하는 수의 개수를 구합니다.
counter = [0, 2, 3, 4, 5]

def 최소값(arr):
    기존값 = 1001
    for x in arr:
        if x < 기존값 and x!=0:
                기존값 = x
    최소=기존값
    return 최소
a = 최소값(counter)
print(a)
