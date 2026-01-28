import pandas as pd

# 차종이 compact, suv인 자동차의 각각 평균 도시 연비 구하기 
mpg = pd.read_csv(r'C:\Users\jaech\Desktop\Python\data\mpg.csv') #mpg파일이 있는 경로 
mpg = mpg.rename(columns={'class' : 'category'}) #변수명이 'class'면 오류날 수 있어서 'category'로 변경
desc = mpg.query('category in ["suv", "compact"]').groupby('category', as_index=False).agg(mean_cty = ('cty', 'mean'))
# print(desc)

#평균 값 간 차이 구하기 
compact = mpg.query('category == "compact"')['cty'] 
suv = mpg.query('category == "suv"')['cty']

from scipy.stats import ttest_ind
t_result = ttest_ind(compact, suv, equal_var = True)
#print(t_result)
#집단 간 차이 유의 O 

# 일반휘발유를 사용하는 자동차와 고급 휘발유를 사용하는 자동차의 각각 평균 도시 연비 구하기 
desc2 = mpg.query('fl in ["r", "p"]').groupby('fl', as_index=False).agg(mean_cty = ('cty', 'mean'))
#print(desc2)

#평균 값 간 차이 구하기 
regular = mpg.query('fl == "r"')['cty']
premium = mpg.query('fl == "p"')['cty']

t_result2 = ttest_ind(regular, premium, equal_var = True)
print(t_result2)
#w집단 간 차이 유의 X 