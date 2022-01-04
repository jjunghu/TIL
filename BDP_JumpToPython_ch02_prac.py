# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 01:24:42 2021

@author: jjunghu
"""

# Q1
a = 80
b = 75
c = 55
(a + b + c)/3     # 70.0

# Q2
if 13%2 == 1:
    print("홀수")
else:
    print("짝수")
# 홀수

# Q3
num = '881120-1068234'
YYYYMMDD = num[:6]
back = num[7:]
print(YYYYMMDD)     # 881120
print(back)         # 1068234

# Q4
pin = "881120-1068234"
i = pin[7]
print(i)       # 1

# Q5
a = "a:b:c:d"
b = a.replace(':','#')
print(b)      # a#b#c#d

# Q6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)      # [5, 4, 3, 2, 1]

# Q7
a = ['Life', 'is', 'too', 'short']
print(" ".join(a))   # Life is too short

# Q8
a = (1, 2, 3) + (4,)    
print(a)        # (1, 2, 3, 4)

# Q9
a = dict()
a

# 1. 
a['name'] = 'python'
a        # {'name': 'python'}
# 2. 
a[('a'),] = 'python'
a        # {('a',): 'python'}
# 3.
a[[1]] = 'python'
# TypeError: unhashable type: 'list'
# 딕셔너리의 Key 값은 변하지 않는 값을 사용해야 한다
# list는 변하는 값이므로 Key의 값에 들어갈 수 없어 오류 발생
# 4. 
a[250] = 'python'
a        # {250: 'python'}

# Q10
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))      # 80

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
list(set(a))       # [1, 2, 3, 4, 5]

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)     # [1, 4, 3]
# a 와 b 는 동일한 리스트를 변수로 갖고 있기 때문에
# a의 리스트에서 1번째 위치가 4로 변경되면 b 리스트도 동일하게 변경된다




