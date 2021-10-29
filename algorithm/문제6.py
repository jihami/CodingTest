'''6.어떤 문자열에 해당단어가 몇개있는지 카운팅
ex) ILOVKEFLOVEE에서 LOV가 몇개 있는지 카운팅'''
string = "ILOVKEFLOVEE"
find = "LOV"
count = 0
#i는 0부터 len(string)-1 만큼 반복
for i in range(len(string)):
    if string[i] == "L":
        if string[i+1] == "O":
            if string[i+2] == "V":
                count += 1

print(count)
