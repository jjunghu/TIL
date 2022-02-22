# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 20:25:29 2022

@author: jjunghu
"""

#%%

# =============================================================================
# =============================================================================
# # 문제 03 유형(DataSet_03.csv 이용)
# 
# 구분자 : comma(“,”), 5,001 Rows, 8 Columns, UTF-8 인코딩
# 안경 체인을 운영하고 있는 한 회사에서 고객 사진을 바탕으로 안경의 사이즈를
# 맞춤 제작하는 비즈니스를 기획하고 있다. 우선 데이터만으로 고객의 성별을
# 파악하는 것이 가능할 지를 연구하고자 한다.
#
# 컬 럼 / 정 의 / Type
# long_hair / 머리카락 길이 (0 – 길지 않은 경우 / 1 – 긴
# 경우) / Integer
# forehead_width_cm / 이마의 폭 (cm) / Double
# forehead_height_cm / 이마의 높이 (cm) / Double
# nose_wide / 코의 넓이 (0 – 넓지 않은 경우 / 1 – 넓은 경우) / Integer
# nose_long / 코의 길이 (0 – 길지 않은 경우 / 1 – 긴 경우) / Integer
# lips_thin / 입술이 얇은지 여부 0 – 얇지 않은 경우 / 1 –
# 얇은 경우) / Integer
# distance_nose_to_lip_long / 인중의 길이(0 – 인중이 짧은 경우 / 1 – 인중이
# 긴 경우) / Integer
# gender / 성별 (Female / Male) / String
# =============================================================================
# =============================================================================

data3 = pd.read_csv('./dataset/DataSet_03.csv')

#%%

# =============================================================================
# 1.이마의 폭(forehead_width_cm)과 높이(forehead_height_cm) 사이의
# 비율(forehead_ratio)에 대해서 평균으로부터 3 표준편차 밖의 경우를 이상치로
# 정의할 때, 이상치에 해당하는 데이터는 몇 개인가? (답안 예시) 10
# =============================================================================

q1 = data3.copy()

q1['forehead_ratio'] = q1['forehead_width_cm']/q1['forehead_height_cm']

xbar = q1['forehead_ratio'].mean()
std=q1['forehead_ratio'].std()

UB = xbar + 3*std
LB = xbar - 3*std

# 이상치 데이터 필터링
q1[(q1['forehead_ratio'] < LB) | (q1['forehead_ratio'] > UB)]

# 이상치 데이터 수
((q1['forehead_ratio'] < LB) | (q1['forehead_ratio'] > UB)).sum()   

# 답: 3


#%%

# =============================================================================
# 2.성별에 따라 forehead_ratio 평균에 차이가 있는지 적절한 통계 검정을 수행하시오.
# - 검정은 이분산을 가정하고 수행한다.
# - 검정통계량의 추정치는 절대값을 취한 후 소수점 셋째 자리까지 반올림하여
# 기술하시오.
# - 신뢰수준 99%에서 양측 검정을 수행하고 결과는 귀무가설 기각의 경우 Y로, 그렇지
# 않을 경우 N으로 답하시오. (답안 예시) 1.234, Y
# =============================================================================

# 두 집단이기에 t-test 진행
# 독립인 2표본 t-검정
# 이분산,등분산이 언급되어있으면 독립인 2표본 t-검정으로 하면 됨

q1.columns
# ['long_hair', 'forehead_width_cm', 'forehead_height_cm', 'nose_wide',
#        'nose_long', 'lips_thin', 'distance_nose_to_lip_long', 'gender',
#        'forehead_ratio']
q1.gender.unique()

g_m = q1[q1.gender == 'Male']['forehead_ratio']
g_f = q1[q1.gender == 'Female']['forehead_ratio']


from scipy.stats import ttest_ind, bartlett

q2_out = ttest_ind(g_m, g_f, equal_var=False)

round(abs(q2_out.statistic), 3)

# 답: 2.999

q2_out.pvalue < 0.01

# 답: Y


# [참고] 등분산 검정
bartlett(g_m, g_f)   # 등분산이다 아니다를 계산
# H0: 등분산
# H1: 등분산이 아니다(-> 이분산)
# pvalue=2.4617792693952707e-48 < 0.05 -> 귀무가설 기각


#%%

# =============================================================================
# 3.주어진 데이터를 사용하여 성별을 구분할 수 있는지 로지스틱 회귀분석을 적용하여
# 알아 보고자 한다. 
# - 데이터를 7대 3으로 나누어 각각 Train과 Test set로 사용한다. 이 때 seed는 123으로
# 한다.
# - 원 데이터에 있는 7개의 변수만 Feature로 사용하고 gender를 label로 사용한다.
# (forehead_forehead_ratio는 사용하지 않음)
# - 로지스틱 회귀분석 예측 함수와 Test dataset를 사용하여 예측을 수행하고 정확도를
# 평가한다. 이 때 임계값은 0.5를 사용한다. 
# - Male의 Precision 값을 소수점 둘째 자리까지 반올림하여 기술하시오. (답안 예시) 
# 0.12
# 
# 
# (참고) 
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn import metrics
# train_test_split 의 random_state = 123
# =============================================================================

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, classification_report

train, test = train_test_split(data3, test_size=0.3, random_state=123)

var_list = data3.columns.drop('gender')

logit = LogisticRegression().fit(train[var_list], train['gender'])

dir(logit)

q3_pred = logit.predict(test[var_list])

q3_pred_pr = logit.predict_proba(test[var_list])
# Female이 0, Male이 1

precision_score(test['gender'], q3_pred, pos_label='Male')

# 답: 0.96

print(classification_report(test['gender'], q3_pred))