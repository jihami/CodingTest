letters = 'python'
print(letters[0],letters[2])

license_plate = "24가 2210"
print(license_plate[-4:])

phone_number = "010-1111-2222"
# 문자열을 다 찾은 다음에 "="을 " "로 대체
# result = ""
# for i in phone_number:
#     if i != "-":
#         result += i
#     else:
#         result += " "
a = phone_number.replace("-"," ")
#새로운 공간을 할당해야함
print(a)

url = "http://sharebook.kr"
# a = url.split(".")
# print(a[-1])
url = "http://share.book.kr"
result = list()
start = 0
for i in range(len(url)) :
    if url[i] == ".":
        result.append(url[start:i])
        start = i+1
result.append(url[start:])
print(result[-1])

t1 = 'python'
t2 = 'java'
print((t1+" "+t2+" ")*4)

상장주식수 = "5,969,782,550"
sam = 상장주식수.replace(",","")
print(int(sam))

ticker = "btc_krw"
result = ticker.split("_")
print(result)