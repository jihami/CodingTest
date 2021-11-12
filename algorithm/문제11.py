'''11.숫자의 갯수가 몇개인지 카운팅
ex) 93728499321에서 9의 갯수 구하기(문자열 사용하지 않고)'''
num = 93728499321
count = 0
# 비효율 적임
# a = str(num)
# for i in a :
#     if i == "9":
#         count += 1
# print(count)
# print(num % 10)
# num = num // 10
# print(num % 10) #.... 마지막 숫자 출력 // -> 몫 연산
while num > 0 :
    # 각 자리의 마지막 숫자를 쪼갬 ( num % 10 )
    if num % 10 == 9 :
        count += 1
    num = num // 10
print(count)