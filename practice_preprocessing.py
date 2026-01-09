# '쉽게 배우는 파이썬 데이터 분석, 김영우, 2022' p194 
import pandas as pd
dt = pd.read_csv('data/mpg.csv') #personal PC data file route. 각자 경로에 맞게 변경해야 함 

dt.loc[[9,13,57,92], 'drv'] = 'k'
dt.loc[[28,42,128,202], 'cty'] = [3,4,39,42] #전처리 연습을 위해 의도적 이상치 할당 

#문제 1번 - 'drv' 변수에 이상치 있는지 확인, 있으면 결측 처리 
#print(dt['drv'].value_counts()) - 이상치 확인 
import numpy as np 
dt['drv'] = np.where(dt['drv'].isin(['4','f','r']), dt['drv'], np.nan)
#print(dt['drv'].value_counts()) 결측치 잘 사라졌나 확인 


#문제 2번 - box plot 활용해 IQR(InterQuartileRange) 벗어난 값 결측 처리  
import seaborn as sb 
import matplotlib.pyplot as mpl
#sb.boxplot(data = dt, y = 'cty')
#mpl.show() #boxplot 출력 

per25 = dt['cty'].quantile(0.25) #14 - 25% 1사분위 수  
per75 = dt['cty'].quantile(0.75) #19 - 75% 3사분위 수 
IQR_dt = per75 - per25 #5 - 3사분위 수 - 1사분위 수 = 중간 50% 범위의 값 

#print(per25 - IQR_dt * 1.5) #6.5 - 하한 절단 기준 
#print(per75 + IQR_dt * 1.5) #26.5 - 상한 절단 기준 

dt['cty'] = np.where((dt['cty'] < 6.5) | (dt['cty'] > 26.5), np.nan, dt['cty'])
#sb.boxplot(data = dt, y = 'cty')
#mpl.show() #정상범위 벗어난 이상값 제거 완료 


#문제 3번 - drv(구동방식)별로 cty(시내연비) 평균이 어떻게 다른지 알아보기. 하나의 pandas 구문으로
print(dt.groupby('drv', as_index= False).agg(cty_mean = ('cty','mean')))