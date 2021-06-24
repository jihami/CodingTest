def solution(char):
    tmp = char[0]

    for i in range(1, len(char)):
        if char[i - 1] != char[i]:
            tmp += char[i]

    return tmp


characters = "senteeeencccccceeee"
print(solution(characters))