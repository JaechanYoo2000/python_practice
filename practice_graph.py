# '쉽게 배우는 파이썬 데이터 분석, 김영우, 2022'

#204p scatter plot 그리기 
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mpl #colab같은 웹과 달리 로컬에서는 반드시 mpl.pyplot 임포트 필요
dt = pd.read_csv('data/mpg.csv') #data file 있는 폴더로 경로 변경

#문제1번 mpg 데이터의 cty(시내연비)와 hwy(고속도로연비) 변수 간 산점도 그리기
#sb.scatterplot(data=dt, x = 'cty', y = 'hwy')
#mpl.show()

#문제2번 midwest 데이터의 poptotal(전체인구)과 popasian(아시아인구) 변수 간 산점도 그리기(범위 제한)
dt2 = pd.read_csv('data/midwest.csv') 
#scplot = sb.scatterplot(data=dt2, x = 'poptotal', y = 'popasian').set(xlim=(0,500000), ylim=(0,10000)) 
#mpl.show()


#211p bar plot 그리기 / mpg 데이터를 사용하므로 dt 그대로 사용 

#문제1번 제조사별 cty 평균이 높은 회사 다섯 곳 막대그래프로 그리기 
dt = dt.rename(columns={'class' : 'category'}) #원본 데이터의 변수명 class는 오류 발생 가능, 이름 변경
dt_bar = dt.query('category == "suv"').groupby('manufacturer').agg(cty_mean = ('cty','mean'))\
    .sort_values('cty_mean', ascending=False).head(5)
#sb.barplot(data=dt_bar, x = 'manufacturer', y = 'cty_mean')
#mpl.show()

#문제2번 자동차 중 어떤 category(자동차 종류)가 많은지 막대그래프로 그리기 
dt_cate_count = dt.groupby('category').agg(category_count = ('category','count'))
#sb.barplot(data = dt_cate_count, x = 'category', y = 'category_count')
#mpl.show()


#217p line plot으로 time series 그리기 

#문제1번 연도별 개인 저축률 변화 시계열 그래프 그리기 
dt3 = pd.read_csv('data/economics.csv')
dt3['date'] = pd.to_datetime(dt3['date']) # read_csv는 문자열로 읽는 게 기본, data time으로 변환 필요 
#sb.lineplot(data=dt3, x = 'date', y = 'psavert')
#mpl.show()

#문제2번 2014년 월별 psavert 변화 시계열 그래프 그리기 
dt3['year'] = dt3['date'].dt.year # 0000-00-00 형식에서 연도만 추출 
dt3['month'] = dt3['date'].dt.month

psavert_2014 = dt3.query('year == 2014')
#sb.lineplot(data = psavert_2014, x = 'month', y = 'psavert')
#mpl.show()


#220p box plot 그리기
#문제1번 mpg 데이터의 class(자동차 종류)별 cty(시내연비) 상자그림 그리기
dt_cate3 = dt.query('category.isin(["compact","subcompact","suv"])')
sb.boxplot(data = dt_cate3, x = 'category', y = 'cty')
mpl.show()