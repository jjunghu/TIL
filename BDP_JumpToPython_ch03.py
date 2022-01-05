# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:17:17 2021

@author: jjunghu
"""

# 03-1. if 조건문
# 참과 거짓을 판단하는 문장
# if 조건문:
#     수행할 문장1
#     수행할 문장2
#     ...
# else:
#     수행할 문장A
#     수행할 문장B
#     ...

money = True

if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# 택시를 타고 가라

# 비교 연산자
# x < y      # x가 y보다 작다
# x > y      # x가 y보다 크다
# x == y     # x와 y가 같다
# x != y     # x와 y가 같지 않다
# x >= y     # x가 y보다 크거나 같다
# x <= y     # x가 y보다 작거나 같다

x = 3
y = 2
x > y     # True
x < y     # False
x == y    # False
x != y    # True

# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라
money = 2000
if money >= 3000:
    print('택시를 타고 가라')
else:
    print('걸어 가라')
# 걸어 가라

# x or y      # 둘 중에 하나만 참이어도 참
# x and y     # 모두 참이면 참
# not x       # x가 거짓이면 참

# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라
money = 2000
card = True
if money >= 3000 or card:
    print('택시를 타고 가라')
else:
    print('걸어 가라')
# 택시를 타고 가라

1 in [1, 2, 3]      # True
1 not in [1, 2, 3]  # False
'a' in ('a', 'b', 'c')     # True
'j' not in 'python'        # True

# 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시를 타고 가라')
else:
    print('걸어 가라')
# 택시를 타고 가라

# 주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')    
#    
# 조건문에서 아무 일도 하지 않게 설정하고 싶다면 pass 사용

# 다양한 조건을 판단하는 elif
# elif는 개수에 제한 없이 사용가능

# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면
# 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타고 가라')
elif card:
    print('택시를 타고 가라')
else:
    print('걸어 가라')
# 택시를 타고 가라

# 03-2. while 반복문
# while 조건문:
#     수행할 문장1
#     수행할 문장2
#     수행할 문장3
#     ...

# 열 번 찍어 안 넘어가는 나무 없다
treeHit = 0
while treeHit < 10 :
    treeHit = treeHit + 1
    print('나무를 %d번 찍었습니다.' % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
        
 # 나무를 1번 찍었습니다.
 # 나무를 2번 찍었습니다.
 # 나무를 3번 찍었습니다.
 # 나무를 4번 찍었습니다.
 # 나무를 5번 찍었습니다.
 # 나무를 6번 찍었습니다.
 # 나무를 7번 찍었습니다.
 # 나무를 8번 찍었습니다.
 # 나무를 9번 찍었습니다.
 # 나무를 10번 찍었습니다.
 # 나무 넘어갑니다.       

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())
# 4를 입력하면 조건문이 거짓이 되어 while문을 빠져나가게 된다.
# number = int(input()) : 사용자의 숫자 입력을 받아들이는 것

coffee = 10 
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    
# 돈을 받았으니 커피를 줍니다.
# 남은 커피의 양은 9개입니다.
# 돈을 받았으니 커피를 줍니다.
# 남은 커피의 양은 8개입니다.
# 돈을 받았으니 커피를 줍니다.
# 남은 커피의 양은 7개입니다.
# 돈을 받았으니 커피를 줍니다.
# 남은 커피의 양은 6개입니다.
# 돈을 받았으니 커피를 줍니다.
# 남은 커피의 양은 5개입니다.
# 돈을 받았으니 커피를 줍니다.
# 남은 커피의 양은 4개입니다.
# 돈을 받았으니 커피를 줍니다.
# 남은 커피의 양은 3개입니다.
# 돈을 받았으니 커피를 줍니다.
# 남은 커피의 양은 2개입니다.
# 돈을 받았으니 커피를 줍니다.
# 남은 커피의 양은 1개입니다.
# 돈을 받았으니 커피를 줍니다.
# 남은 커피의 양은 0개입니다.
# 커피가 다 떨어졌습니다. 판매를 중지합니다.

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    
# while문의 맨 처음으로 돌아가기
a = 0 
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
# 1
# 3
# 5
# 7
# 9
# continue문은 while문의 맨 처음(조건문: a<10)으로 돌아가게 하는 명령어
# a가 짝수이면 print(a)는 수행되지 않을 것

# 03-3. for 반복문
# for 변수 in 리스트 (또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2
#     ...
# 리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로
# 변수에 대입되어 "수행할 문장1", "수행할 문장2" 등이 수행

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)    
# one
# two
# three    

a = [(1,2), (3,4), (5,6)]
for (first, last) in a :
    print(first + last)
# 3
# 7
# 11

# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 학격
# 그렇지 않으면 불합격. 합격인지 불합격인지 결과를 보여주시오.

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입닌다." % number)
# 1번 학생은 합격입니다.
# 2번 학생은 불합격입닌다.
# 3번 학생은 합격입니다.
# 4번 학생은 불합격입닌다.
# 5번 학생은 합격입니다.   

# for문과 continue
# 60점 이상인 사람에게는 축하메시지를 보내고
# 나머지 사람에게는 아무 메시지도 전하지 않는 프로그램
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)
# 1번 학생 축하합니다. 합격입니다.
# 3번 학생 축하합니다. 합격입니다.
# 5번 학생 축하합니다. 합격입니다.

# for문과 함께 자주 사용하는 range 함수
# range 함수 : 숫자 리스트를 자동으로 만들어줌
# range(시작 숫자, 끝 숫자) >> 끝 숫자는 포함되지 않음
a = range(10)
a      # range(0, 10) : 0부터 10 '미만'의 숫자
a = range(1,11)     # 1부터 11미만의 숫자(11은 포함X)

add = 0
for i in range(1, 11):
    add = add + i
print(add)        # 55 >> 최종적 add만 출력

add = 0
for i in range(1, 11):
    add = add + i
    print(add)
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# 55
# 위와 차이 비교하기

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))
# 1번 학생 축하합니다. 합격입니다.
# 3번 학생 축하합니다. 합격입니다.
# 5번 학생 축하합니다. 합격입니다.

# len(marks) == 5, range(len(marks)) == range(5)
# number 변수에는 차례로 0부터 4까지의 숫자가 대입
# marks[number]: 인덱스, %d에 대입되는 number는 +1 해줘야함

# for와 range를 이용한 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')

# 2 4 6 8 10 12 14 16 18 
# 3 6 9 12 15 18 21 24 27 
# 4 8 12 16 20 24 28 32 36 
# 5 10 15 20 25 30 35 40 45 
# 6 12 18 24 30 36 42 48 54 
# 7 14 21 28 35 42 49 56 63 
# 8 16 24 32 40 48 56 64 72 
# 9 18 27 36 45 54 63 72 81 

# 매개변수 end를 넣어 준 이유는 해당 결과값을 출력할 때
# 다음줄로 넘기지 않고 그 줄에 계속해서 출력하기 위함
# print(' ')는 2단,3단 등을 구분하기 위해
# for문이 끝나면 결과값을 다음 줄부터 출력하게 해주는 문장

# 리스트 내포(List comprehension)
# [표현식 for 항목 in 반복가능객체 if 조건문]
# if 조건 부분은 생략가능

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)
# [3, 6, 9, 12]

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)
# [3, 6, 9, 12]    >> 리스트 내포를 사용한 방법

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
# [6, 12] 

# 구구단의 모든 결과를 리스트에 담고 싶다면
result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24,
#  27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 
#  35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 
#  35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 
#  27, 36, 45, 54, 63, 72, 81]




































    
    
    
    
    





    
    
    
    




