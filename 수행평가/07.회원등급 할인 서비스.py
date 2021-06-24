def solution(price, grade):
    answer = 0
    if grade == "S":
        answer = int(price*0.95)
    elif grade == "G":
        answer = int(price*0.9)
    elif grade == "V":
        answer = int(price*0.85)
    return answer
price1 = 2500
grade1 = "V"
print(solution(price1,grade1))
price2 = 96900
grade2 = "S"
print(solution(price2,grade2))