###########################
# 라이브러리 사용
import pandas as pd

###########################
# 파일로부터 데이터 읽어오기
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
레모네이드 = pd.read_csv(파일경로)


###########################
# 데이터의 모양확인
print(레모네이드.shape)

###########################
# 데이터 칼럼이름 확인
print(레모네이드.columns)

###########################
# 독립변수와 종속변수 분리
독립 = 레모네이드[['온도']]
종속 = 레모네이드[['판매량']]


###########################
# 각각의 데이터 확인해보기
print(레모네이드.head())