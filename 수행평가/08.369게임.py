def solution(num):
    cnt = 0

    for i in range(1, num + 1):
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            cnt += 1
        if i // 10 % 10 == 3 or i // 10 % 10 == 6 or i // 10 % 10 == 9:
            cnt += 1
        if i // 100 % 10 == 3 or i // 100 % 10 == 6 or i // 100 % 10 == 9:
            cnt += 1
    return cnt
number = 40
print(solution(number))