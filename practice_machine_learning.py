import pandas as pd
adult = pd.read_csv(r'C:\Users\jaech\Desktop\Python\data\adult.csv')

#adult 데이터 파일을 활용하여 imcome(연소득)을 예측하는 모델 만들기 
#전처리
import numpy as np
adult['income'] = np.where(adult['income'] == '>50K', 'high','low') #변수 값에 특수문자나 대소문자 있으면 불편해 변경 
adult = adult.drop(columns = 'fnlwgt') #예측에 불필요한 변수 제거 

#문자 타입 변수를 숫자 타입으로 변환, 원핫 인코딩(더미변수로 변환)
adult_sex = adult[['sex']]
adult_sex = pd.get_dummies(adult_sex) #datatype이 bool(boolean)으로 변환됨 값의 범위가 True/False

target = adult['income']
adult = adult.drop(columns = 'income')
adult = pd.get_dummies(adult) #imcome 변수 말고 모두 원핫 인코딩 수행 

adult['income'] = target 
#adult.info(max_cols = np.inf)


#학습용/검증용 데이터셋 분리
from sklearn.model_selection import train_test_split
adult_train, adult_test = train_test_split(adult, test_size = 0.3, stratify = adult['income'], random_state = 1234)

#모델 설정하기 
from sklearn import tree 
clf = tree.DecisionTreeClassifier(max_depth = 3, random_state = 1234)

#모델 만들기 
train_x = adult_train.drop(columns = 'income')
train_y = adult_train['income']

model = clf.fit(X = train_x, y = train_y) 

# 완성된 의사결정나무 그래프로 나타내기
import matplotlib.pyplot as plt 
plt.rcParams.update({'figure.dpi' : '100', 'figure.figsize' : [12, 8]})
#tree.plot_tree(model,feature_names= list(train_x.columns), class_names = ['high','low'], proportion= True, filled = True,\
    #rounded = True, impurity= False, label = 'root', fontsize = 10)
#plt.show();

# 완성된 모델을 이용해 예측하기 
test_x = adult_test.drop(columns = 'income')
test_y = adult_test['income'] 
adult_test['pred'] = model.predict(test_x)
#print(adult_test) income 변수 값과 pred 변수 값이 일치하면 예측이 맞은 것 

# 성능평가 - confusion matrix(혼동행렬) 만들기
from sklearn.metrics import confusion_matrix
conf_mat = confusion_matrix(y_true = adult_test['income'], y_pred = adult_test['pred'], labels = ['high','low'])

plt.rcParams.update(plt.rcParamsDefault)

from sklearn.metrics import ConfusionMatrixDisplay
p = ConfusionMatrixDisplay(confusion_matrix = conf_mat, display_labels = ('high','low'))
p.plot(cmap = 'Blues')
#plt.show()

# 성능평가 - 정확도(Accuracy) 구하기 
import sklearn.metrics as mt 
accuracy = mt.accuracy_score(y_true = adult_test['income'], y_pred = adult_test['pred'])
#print(accuracy)

# 성능평가 - 정밀도(Precision) 구하기 
precision = mt.precision_score(y_true = adult_test['income'], y_pred = adult_test['pred'], pos_label = 'high')
#print(precision)

# 성능평가 - 재현율(Recall) 구하기 
recall = mt.recall_score(y_true = adult_test['income'], y_pred = adult_test['pred'], pos_label = 'high')
#print(recall)

# 성능평가 - F1 스코어 구하기
f1 = mt.f1_score(y_true = adult_test['income'], y_pred = adult_test['pred'], pos_label = 'high')
#print(f1)