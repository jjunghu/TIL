# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:41:06 2022

@author: jjunghu
"""

#%%

# =============================================================================
# =============================================================================
# # 문제 02 유형(DataSet_02.csv 이용)
# 구분자 : comma(“,”), 200 Rows, 6 Columns, UTF-8 인코딩

# 환자의 상태와 그에 따라 처방된 약에 대한 정보를 분석하고자한다
# 
# 컬 럼 / 정 의  / Type
# Age  / 연령 / Integer
# Sex / 성별 / String
# BP / 혈압 레벨 / String
# Cholesterol / 콜레스테롤 레벨 /  String
# Na_to_k / 혈액 내 칼륨에 대비한 나트륨 비율 / Double
# Drug / Drug Type / String
# =============================================================================
# =============================================================================

import pandas as pd
import numpy as np

data2 = pd.read_csv('./dataset/DataSet_02.csv')
data2.info()


#%%

# =============================================================================
# 1.해당 데이터에 대한 EDA를 수행하고, 여성으로 혈압이 High, Cholesterol이 Normal인
# 환자의 전체에 대비한 비율이 얼마인지 소수점 네 번째 자리에서 반올림하여 소수점 셋째
# 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================

data2.columns
# ['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K', 'Drug']

var_list = ['Sex', 'BP', 'Cholesterol']
q1 = data2[var_list].value_counts(normalize=True)
q1

q1[('F', 'HIGH', 'NORMAL')]

# 답: 0.105


# 내 풀이)
# value1 = sum((data2['Sex']=='F') & (data2['BP']=='HIGH') & (data2['Cholesterol']=='NORMAL'))
# total = data2['Sex'].count()

# forehead_ratio = round((value1/total), 3)

# # 답: 0.105


#%%

# =============================================================================
# 2. Age, Sex, BP, Cholesterol 및 Na_to_k 값이 Drug 타입에 영향을 미치는지 확인하기
# 위하여 아래와 같이 데이터를 변환하고 분석을 수행하시오. 
# - Age_gr 컬럼을 만들고, Age가 20 미만은 ‘10’, 20부터 30 미만은 ‘20’, 30부터 40 미만은
# ‘30’, 40부터 50 미만은 ‘40’, 50부터 60 미만은 ‘50’, 60이상은 ‘60’으로 변환하시오. 
# - Na_K_gr 컬럼을 만들고 Na_to_k 값이 10이하는 ‘Lv1’, 20이하는 ‘Lv2’, 30이하는 ‘Lv3’, 30 
# 초과는 ‘Lv4’로 변환하시오.
# - Sex, BP, Cholesterol, Age_gr, Na_K_gr이 Drug 변수와 영향이 있는지 독립성 검정을
# 수행하시오.
# - 검정 수행 결과, Drug 타입과 연관성이 있는 변수는 몇 개인가? 연관성이 있는 변수
# 가운데 가장 큰 p-value를 찾아 소수점 여섯 번째 자리 이하는 버리고 소수점 다섯
# 번째 자리까지 기술하시오.
# (답안 예시) 3, 1.23456
# =============================================================================

q2 = data2.copy()

# 변수 생성
q2['Age_gr'] = np.where(q2.Age < 20, 10, 
                np.where(q2.Age < 30, 20,
                    np.where(q2.Age < 40, 30,
                    np.where(q2.Age < 50, 40,
                    np.where(q2.Age<60, 50, 60)))))

q2['Na_K_gr'] = np.where(q2.Na_to_K <=10, 'Lv1',
                    np.where(q2.Na_to_K <=20, 'Lv2',
                        np.where(q2.Na_to_K <=30, 'Lv3', 'Lv4')))


# 교차표 작성
q2.columns
# ['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K', 'Drug', 'Age_gr',
#    'Na_K_gr']

temp = pd.crosstab(index=q2['Sex'],
                   columns=q2['Drug'])

# 카이스퀘어 검정
from scipy.stats import chi2_contingency

q2_out = chi2_contingency(temp)
q2_out[1]   # p-value


# 반복 적용

value_list = ['Age', 'Sex', 'BP', 'Cholesterol', 'Age_gr', 'Na_K_gr']

q2_out2=[]

for i in value_list:
    temp = pd.crosstab(index=q2[i],
                       columns=q2['Drug'])
    q2_out = chi2_contingency(temp)
    chi2 = q2_out[0]
    pvalue = q2_out[1]
    q2_out2.append([i, chi2, pvalue])

q2_out2 = pd.DataFrame(q2_out2, columns=['var', 'chi2', 'pvalue'])

# 영향력 있는 변수 추출
q2_out3 = q2_out2[q2_out2.pvalue < 0.05]
len(q2_out3)    # 4

# 영향력 있는 변수 중 가장 큰: p-value

q2_out3.pvalue.max()    #  0.0007010113024729462

# 답: 4, 0.00070


#%%

# =============================================================================
# 3.Sex, BP, Cholesterol 등 세 개의 변수를 다음과 같이 변환하고 의사결정나무를 이용한
# 분석을 수행하시오.
# - Sex는 M을 0, F를 1로 변환하여 Sex_cd 변수 생성
# - BP는 LOW는 0, NORMAL은 1 그리고 HIGH는 2로 변환하여 BP_cd 변수 생성
# - Cholesterol은 NORMAL은 0, HIGH는 1로 변환하여 Ch_cd 생성
# - Age, Na_to_k, Sex_cd, BP_cd, Ch_cd를 Feature로, Drug을 Label로 하여 의사결정나무를
# 수행하고 Root Node의 split feature와 split value를 기술하시오. 
# 이 때 split value는 소수점 셋째 자리까지 반올림하여 기술하시오. (답안 예시) Age, 
# 12.345
# =============================================================================

q3 = data2.copy()

# 변수 생성
q3['Sex_cd'] = np.where(q3.Sex == 'M', 0, 1)
q3['BP_cd'] = np.where(q3.BP == 'LOW', 0, 
                       np.where(q3.BP == 'NORMAL', 1, 2 ))
q3['Ch_cd'] = np.where(q3.Cholesterol == 'NORMAL', 0, 1)                     


# 의사결정나무 실행 -> 모델 생성
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text

var_list = ['Age', 'Na_to_K', 'Sex_cd', 'BP_cd', 'Ch_cd']

dt = DecisionTreeClassifier().fit(q3[var_list], q3['Drug'])


#  Root Node의 split feature와 split value

plot_tree(dt, max_depth=2, feature_names=var_list,
          class_names=list(q3.Drug.unique()),
            precision=3,
            fontsize=8)

print(export_text(dt, feature_names=var_list, decimals=3))

# 답: Na_to_K, 14.829


