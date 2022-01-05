# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 18:47:50 2021

@author: jjunghu
"""

# 03장 연습문제
# Q1
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif 'python' in a and 'you' not in a: print('python')
elif 'shirt' not in a: print('shirt')
elif 'need' in a: print('need')
else: print('none')

# shirt     >> need도 만족하지만 그 전에 shirt가 먼저 만족되므로 shirt만 출력


# Q2
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result = result + i
    i = i + 1
print(result)        # 166833


# Q3
i = 1
while i <= 5:
    star = '*' * i
    i = i + 1
    print(star)

# *
# **
# ***
# ****
# *****

# 풀이 방법
i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)


# Q4
for i in range(1,101):
    print(i)


# Q5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in A:
    total += score    
average = total / len(A)
print(average)

# 79.0


# Q6
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)
# [2, 6, 10]

