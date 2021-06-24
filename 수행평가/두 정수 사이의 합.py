def solution(a, b):
    answer = 0
    if a == b:
        return a
    elif a > b:
        for i in range(b, a+1):
            answer += i
        return answer
    else:
        for i in range(a, b+1):
            answer += i
        return answer

a1 = 3
b1 = 5
print(solution(a1, b1))
a2 = 3
b2 = 3
print(solution(a2, b2))
a3 = 5
b3 = 3
print(solution(a3, b3))