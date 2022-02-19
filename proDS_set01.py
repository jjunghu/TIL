# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:36:22 2022

@author: jjunghu
"""

#%%

# =============================================================================
# =============================================================================
# # 문제 01 유형(DataSet_01.csv 이용)
#
# 구분자 : comma(“,”), 4,572 Rows, 5 Columns, UTF-8 인코딩
# 
# 글로벌 전자제품 제조회사에서 효과적인 마케팅 방법을 찾기
# 위해서 채널별 마케팅 예산과 매출금액과의 관계를 분석하고자
# 한다.
# 컬 럼 / 정 의  /   Type
# TV   /     TV 마케팅 예산 (억원)  /   Double
# Radio / 라디오 마케팅 예산 (억원)  /   Double
# Social_Media / 소셜미디어 마케팅 예산 (억원)  / Double
# Influencer / 인플루언서 마케팅
# (인플루언서의 영향력 크기에 따라 Mega / Macro / Micro / 
# Nano) / String

# SALES / 매출액 / Double
# =============================================================================
# =============================================================================

import pandas as pd
import numpy as np

data1 = pd.read_csv('./dataset/Dataset_01.csv')
data1.info()
data1.columns
# ['TV', 'Radio', 'Social_Media', 'Influencer', 'Sales']

#%%

# =============================================================================
# 1. 데이터 세트 내에 총 결측값의 개수는 몇 개인가? (답안 예시) 23
# =============================================================================

data1.isna().sum().sum()

# 답: 26

# [참고] 결측치가 포함된 행을 찾기
data1.isna().any(axis=1).sum()  # 결측치가 하나라도 있는 행 찾기
# 답: 26

#%%

# =============================================================================
# 2. TV, Radio, Social Media 등 세 가지 다른 마케팅 채널의 예산과 매출액과의 상관분석을
# 통하여 각 채널이 매출에 어느 정도 연관이 있는지 알아보고자 한다. 
# - 매출액과 가장 강한 상관관계를 가지고 있는 채널의 상관계수를 소수점 5번째
# 자리에서 반올림하여 소수점 넷째 자리까지 기술하시오. (답안 예시) 0.1234
# =============================================================================

var_list = ['TV', 'Radio', 'Social_Media', 'Sales']

q2 = data1[var_list].corr().abs().drop('Sales')['Sales']  
# Sales는 자기자신이므로 상관관계가 1로 가장 커서 제거

q2.max()  # 최대값
round(q2.max(), 4)

# 답: 0.9995

# [참고]
q2.nlargest(1)  # 상위 n개의 값
q2.argmax()   # 최대값이 있는 위치번호
q2.idxmax()   # 최대값이 있는 인덱스명



#%%

# =============================================================================
# 3. 매출액을 종속변수, TV, Radio, Social Media의 예산을 독립변수로 하여 회귀분석을
# 수행하였을 때, 세 개의 독립변수의 회귀계수를 큰 것에서부터 작은 것 순으로
# 기술하시오. 
# - 분석 시 결측치가 포함된 행은 제거한 후 진행하며, 회귀계수는 소수점 넷째 자리
# 이하는 버리고 소수점 셋째 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================

from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols
from statsmodels.api import OLS, add_constant

# LinearRegression

q3 = data1.dropna()
var_list = ['TV', 'Radio', 'Social_Media']

# lm = LinearRegression(fit_intercept=True).fit(X,y)
lm = LinearRegression(fit_intercept=True)
lm.fit(q3[var_list], q3['Sales'])

dir(lm)

lm.intercept_  # 절편
lm.coef_  # 회귀계수
# [ 3.56256963, -0.00397039,  0.00496402]

# ols

# lm2 = ols(form, data)
# lm3 = lm2.fit()   # lm2에 다시 넣으면 안됨, 구조가 다르기때문에 ols기능 상실
# lm2 = ols(form, data).fit()   # 이 방식을 많이 사용

# form : 'y~x1+C(x2)+x3-1'  # 상수항(절편) 제거하고 싶으면 -1

form1 = 'Sales~'+'+'.join(var_list)
print(form1)   # Sales~TV+Radio+Social_Media

lm2 = ols(form1, q3).fit()

dir(lm2)
lm2.summary()   # 상세한 정보

# OLS : 기본적으로 절편 미포함, 
# - 절편 구할 수 있도록 1만 들어가있는 상수항 변수 추가해야 함(add_constant)

X = add_constant(q3[var_list])
lm3 = OLS(q3['Sales'], X).fit()   # y,X 순서로 들어감
lm3.summary()

lm2.params
lm2.pvalues[lm2.pvalues < 0.05]

lm2.params.drop('Intercept').sort_values(ascending=False)

# 답:
# TV              3.562570
# Social_Media    0.004964
# Radio          -0.003970