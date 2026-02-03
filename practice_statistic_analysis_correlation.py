import pandas as pd
econo = pd.read_csv(r'C:\Users\jaech\Desktop\Python\data\economics.csv')
cor = econo[['unemploy', 'pce']].corr() #실업자 수와 개인 소비 지출(pce) 간 상관계수 구하기
#print(cor) 상관계수 출력

#유의확률도 함께 구하기 
from scipy.stats import pearsonr
pearsonr_result = pearsonr(econo['unemploy'], econo['pce'])
#print(pearsonr_result) #상관계수와 p-value 출력

#상관행렬 만들기 
df = pd.DataFrame({ 'math' : [60,80,50,90,100], 'Korean' : [70,90,40,90,100], 'English' : [30,75,65,100,90] }) #임시 데이터프레임
df_cor = df.corr()
#print(df_cor) # 상관행렬 출력 

#상관행렬 히트맵 만들기 
import matplotlib.pyplot as plt 
import seaborn as sb
plt.rcParams.update({'figure.dpi' : '120', 'figure.figsize' : [7.5,5.5]})   #해상도, 가로세로 비율 설정 
sb.heatmap(df_cor, annot=True, cmap = 'RdBu')
plt.show() #히트맵 출력 