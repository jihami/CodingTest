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

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)

movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[-2]
# for x in movie_rank:
#     if x == "럭키":
#         movie_rank.remove("럭키")
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨', '럭키']
result = list()
for x in movie_rank: #중복 허용 x
    if x != "럭키":
        result.append(x)
    else:
        continue
print(result)

nums = [1, 2, 3, 4, 5]
print(sum(nums))

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# print(len(cook)) #중복 허용 ver
# a=set(cook) #set이 중복 제거해줌
# print(len(a))
# resultc = list() #반복분 코드
# for x in cook:
#     if x not in resultc:
#         resultc.append(x)
#     else:
#         continue
# ac=len(resultc)
# print(ac)
resultc = dict() #딕셔너리
for x in cook:
    resultc[x] = 1
ac=len(resultc)
print(ac)


nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))

nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)