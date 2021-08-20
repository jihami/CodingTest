setence1 = "naver odd or even."
str = ' '
#문자열에 있는거 하나씩 출력
for x in setence1:
    if x != '.' and x != ' ': #이거 뺴고 출력
        str += x
    print(str)