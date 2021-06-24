def solution(scores):
    cnt = 0

    for i in scores:
        if i >= 650 and i < 800:
            cnt += 1

    return cnt


scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
print(solution(scores))