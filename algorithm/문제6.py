'''6.어떤 문자열에 해당단어가 몇개있는지 카운팅
ex) ILOVKEFLOVEE에서 LOV가 몇개 있는지 카운팅'''
string = "ILOVKEFLOVEE"
find = "LOV"
count = 0

#Q1. 일반화된 코드가 아닌이유 : find 문자열의 길이에 따라 코드가 달라짐

#Q2. 결함 : i+1 ... 떄문에 인덱스 길이를 넘어갈 수 있음

#i는 0부터 len(string)-1 만큼 반복
# for i in range(len(string)):
#     # if string[i] == "L": Q2 결함
#     if string[i] == "L" and i+len(find) <= len(string):
#         if string[i+1] == "O":
#             if string[i+2] == "V":
#                 count += 1
#
# print(count)
string = "ILOVKEFLOVEEL"
find = "LOV"
print( string.count(find) )