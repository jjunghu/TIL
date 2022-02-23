# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:20:02 2022

@author: jjunghu
"""

#%%

# =============================================================================
# =============================================================================
# # 문제 04 유형(DataSet_04.csv 이용)
#
#구분자 : comma(“,”), 6,718 Rows, 4 Columns, UTF-8 인코딩

# 한국인의 식생활 변화가 건강에 미치는 영향을 분석하기에 앞서 육류
# 소비량에 대한 분석을 하려고 한다. 확보한 데이터는 세계 각국의 1인당
# 육류 소비량 데이터로 아래와 같은 내용을 담고 있다.

# 컬 럼 / 정 의 / Type
# LOCATION / 국가명 / String
# SUBJECT / 육류 종류 (BEEF / PIG / POULTRY / SHEEP) / String
# TIME / 연도 (1990 ~ 2026) / Integer
# Value / 1인당 육류 소비량 (KG) / Double
# =============================================================================
# =============================================================================

# (참고)
# #1
# import pandas as pd
# import numpy as np
# #2
# from scipy.stats import ttest_rel
# #3
# from sklearn.linear_model import LinearRegression

#%%

import pandas as pd
import numpy as np

data4 = pd.read_csv('./dataset/Dataset_04.csv')

# =============================================================================
# 1.한국인의 1인당 육류 소비량이 해가 갈수록 증가하는 것으로 보여 상관분석을 통하여
# 확인하려고 한다. 
# - 데이터 파일로부터 한국 데이터만 추출한다. 한국은 KOR로 표기되어 있다.
# - 년도별 육류 소비량 합계를 구하여 TIME과 Value간의 상관분석을 수행하고
# 상관계수를 소수점 셋째 자리에서 반올림하여 소수점 둘째 자리까지만 기술하시오. 
# (답안 예시) 0.55
# =============================================================================

data4.columns
# ['LOCATION', 'SUBJECT', 'TIME', 'Value']

q1 = data4[data4.LOCATION=='KOR']

q1_out = q1.groupby('TIME')['Value'].sum().reset_index().corr()

q1_out['TIME']['Value']

# 답: 0.96
#%%

# =============================================================================
# 2. 한국 인근 국가 가운데 식생의 유사성이 상대적으로 높은 일본(JPN)과 비교하여, 연도별
# 소비량에 평균 차이가 있는지 분석하고자 한다.
# - 두 국가의 육류별 소비량을 연도기준으로 비교하는 대응표본 t 검정을 수행하시오.
# - 두 국가 간의 연도별 소비량 차이가 없는 것으로 판단할 수 있는 육류 종류를 모두
# 적으시오. (알파벳 순서) (답안 예시) BEEF, PIG, POULTRY, SHEEP
# =============================================================================

# 한국, 일본 필터링
q2 = data4[data4.LOCATION.isin(['KOR', 'JPN'])]

# 육류 종류 목록
sub_list = q2.SUBJECT.unique()
# ['BEEF', 'PIG', 'POULTRY', 'SHEEP']

# 참고
temp = q2[q2.SUBJECT == 'BEEF']
q2_tab = pd.pivot_table(temp, index='TIME',
                        columns = 'LOCATION',
                        values = 'Value')


# 반복문을 이용해서 육류 종류별로 빈도 작성 후 결측치 포함 행 제거
from scipy.stats import ttest_rel

q2_out = []

for i in sub_list:
    temp = q2[q2.SUBJECT == i]
    q2_tab = pd.pivot_table(temp, index='TIME',
                            columns = 'LOCATION',
                            values = 'Value').dropna()
    ttest_out = ttest_rel(q2_tab['KOR'], q2_tab['JPN'])
    pvalue = ttest_out.pvalue
    q2_out.append([i, pvalue])

q2_out = pd.DataFrame(q2_out, columns=['var', 'pvalue'])

q2_out[q2_out.pvalue >= 0.05]   # 차이가 없다-> 귀무가설을 기각 안하는 것

# 답: POULTRY


#%%

# =============================================================================
# 3.(한국만 포함한 데이터에서) Time을 독립변수로, Value를 종속변수로 하여 육류
# 종류(SUBJECT) 별로 회귀분석을 수행하였을 때, 가장 높은 결정계수를 가진 모델의
# 학습오차 중 MAPE를 반올림하여 소수점 둘째 자리까지 기술하시오. (답안 예시) 21.12
# (MAPE : Mean Absolute Percentage Error, 평균 절대 백분율 오차)
# (MAPE = Σ ( | y - y ̂ | / y ) * 100/n ))
# 
# =============================================================================
data4.columns

q3 = data4[data4.LOCATION == 'KOR']

sub_list = q3.SUBJECT.unique()


from sklearn.linear_model import LinearRegression

q3_out=[]

for i in sub_list:
    temp = q3[q3.SUBJECT == i]
    lm = LinearRegression().fit(temp[['TIME']], temp['Value'])
    r2_score = lm.score(temp[['TIME']], temp['Value'])
    pred = lm.predict(temp[['TIME']])
    # MAPE = Σ ( | y - y ̂ | / y ) * 100/n 
    mape = (abs(temp['Value'] - pred) / temp['Value']).sum() * 100/len(temp)
    q3_out.append([i, r2_score, mape])
    
q3_out = pd.DataFrame(q3_out, columns=['sub', 'r2_score', 'mape'])

q3_out.loc[q3_out.r2_score.idxmax(), 'mape']

# 답: 5.78

    
# [참고]
q3[['TIME']].shape

q3['TIME'].values.reshape(-1,1).shape
# 데이터프레임은 바로 reshape 사용 못함(numpy array에서만 바로 사용가능)
    

