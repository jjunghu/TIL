# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:52:42 2021

@author: jjunghu
"""

# 02-1 숫자형
# 정수형 Integer
a = 123
a = -178
a = 0

# 실수형 Floating point (소수점이 포함된 숫자)
a = 1.2
a = -3.45

# 사칙연산 + - * /
a = 3
b = 4
a + b
a * b
a / b

# 제곱 연산 **
a = 3
b = 4
a ** b

# 나눗셈 나머지 %
7 % 3     # 1 >> 나머지 반환
3 % 7     # 3 >> 나머지 반환

# 나눗셈 몫 //
7 // 4   # 1 >> 몫 반환


# 02-2 문자열 자료형
# 문자열 연산
head = "Python"
tail = " is fun!"
head + tail         # 'Python is fun!' 문자열 더하기

a = "python"
a * 2               # 'pythonpython' 문자열 곱하기

print("=" * 50)
print("My Program")
print("=" * 50)
# ==================================================
# My Program
# ==================================================

# 문자열 길이 len()
a = "Life is too short"
len(a)

# 문자열 인덱싱(indexing)
a = "Life is too short, You need Python"
a[3]      # 'e' (Life 에서의 e) 
a[-1]     # 'n' (뒤에서부터 첫번째)
# a[번호] : 인덱싱 indexing

# 파이썬은 0부터 숫자를 센다

# 문자열 슬라이싱(Slicing)
a = "Life is too short, You need Python"
a[0:4]      # 'Life'
a[0:3]      # 'Lif'
a[5:7]      # 'is'
a[12:17]    # 'short'
# a[n,m] : 슬라이싱 slicing >> n부터 m-1번째까지 문자열 추출

a[19:]      # 'You need Python'
a[:17]      # 'Life is too short'
a[:]        # 'Life is too short, You need Python'
a[19:-7]    # 'You need'

# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
date       # '20010331'
weather    # 'Rainy'

a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
year      # '2001'
day       # '0331'
weather   # 'Rainy'

a = "Pithon"
a[:1]       # 'P'
a[2:]       # 'thon'
a[:1] + 'y' + a[2:]  # 'Python'

# 문자열 포매팅 Formatting
# 숫자 바로 대입
"I eat %d apples." % 3        # 'I eat 3 apples.'

# 문자열 바로 대입
"I eat %s apples." % "five"   # 'I eat five apples.'

# 숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." % number   # 'I eat 3 apples.'

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number,day)
# 'I ate 10 apples. so I was sick for three days.'

# 문자열 포맷코드
# %s : 문자열 String
# %c : 문자 1개 character
# %d : 정수 Integer
# %f : 부동소수 floating point >> 실수
# %o : 8진수
# %x : 16진수
# %% : Literal % (문자 % 자체)

"I have %s apples" %3     # 'I have 3 apples'
"rate is %s" %3.234       # 'rate is 3.234'
# %s 는 어떤 형태의 값이든 변환해 넣을 수 있음

"Error is %d%" %98    # incomplete format 값 오류
"Error is %d%%" %98   # 'Error is 98%'

# 정렬과 공백
"%10s" % "hi"      
# '        hi'
# 전체 길이가 10개인 문자열 공간에서 대입되는 값을 
# 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨두라는 의미
"%-10sjane" % 'hi'
# 'hi        jane'
# hi를 왼쪽으로 정렬하고 나머지는 공백

# 소수점 표현하기
"%0.4f" % 3.42134234   # '3.4213' >> 소수점 뒤 4자리 ('.'은 소수점 포인트)
"%10.4f" % 3.42134234  # '    3.4213'
# 소수점 네 번째 자리까지 표시, 전체길이 10개, 오른쪽 정렬

# format 함수를 사용한 포매팅
"I eat {0} apples".format(3)        # 'I eat 3 apples'
"I eat {0} apples".format("five")   # 'I eat five apples'

number = 3
"I eat {0} apples".format(number)   # 'I eat 3 apples'

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number,day)
# 'I ate 10 apples. so I was sick for three days.'

"I ate {number} apples. so I was sick for {day} days.".format(number=10,day=3)
# 'I ate 10 apples. so I was sick for 3 days.'

"I ate {0} apples. so I was sick for {day} days.".format(10,day=3)
# 'I ate 10 apples. so I was sick for 3 days.'

"{0:<10}".format("hi")
# 'hi        '
# 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로

"{0:>10}".format("hi")
# '        hi'
# 오른쪽으로 정렬, 총 자릿수 10

"{0:^10}".format("hi")
# '    hi    '
# 가운데 정렬

# 공백 채우기
"{0:=^10}".format("hi")     # '====hi===='
"{0:!<10}".format("hi")     # 'hi!!!!!!!!'

# 소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y)        # '3.4213'
"{0:10.4f}".format(y)       # '    3.4213'

# f 문자열 포매팅
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
# '나의 이름은 홍길동입니다. 나이는 30입니다.'

age = 30
f'나는 내년이면 {age+1}살이 된다'
# '나는 내년이면 31살이 된다'

d = {'name':'홍길동', 'age' : 30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
# '나의 이름은 홍길동입니다. 나이는 30입니다.'
# 딕셔너리는 Key와 Value를 한 쌍으로 갖는 자료형

f'{"hi":<10}'   # 'hi        ' : 왼쪽 정렬
f'{"hi":>10}'   # '        hi' : 오른쪽 정렬
f'{"hi":^10}'   # '    hi    ' : 가운데 정렬

f'{"hi":=^10}'  # '====hi===='
f'{"hi":!<10}'  # 'hi!!!!!!!!'

y = 3.42134234
f'{y:0.4f}'     # '3.4213' 
f'{y:10.4f}'    # '    3.4213'

# 문자열 관련 함수들 (내장 함수)
# 문자 개수 세기 count
a = "hobby"
a.count('b')      # 2

# 위치 찾기 find
a = "Python is the best choice"
a.find('b')       # 14 : 문자 b가 처음으로 나온 위치 반환
a.find('k')       # -1 : 존재하지 않는다면 -1 반환

# 위치 알려주기 index
a = "Life is too short"
a.index('t')      # 8 : 문자 t가 맨 처음으로 나온 위치 반환
a.index('k')      # substring not found : 존재하지 X

# 문자열 삽입 join
",".join('abcd')              # 'a,b,c,d'
",".join(['a','b','c','d'])   # 'a,b,c,d'

a = "hi"
a.upper()     # 'HI' : 대문자로 바꾸기
a.lower()     # 'hi' : 소문자로 바꾸기

a = " hi "
a.lstrip()    # 'hi ' : 왼쪽 공백 지우기
a.rstrip()    # ' hi' : 오른쪽 공백 지우기
a.strip()     # 'hi'  : 양쪽 공백 지우기

# 문자열 바꾸기 replace
a = "Life is too short"
a.replace("Life", "Your leg")
# 'Your leg is too short'
# replace("바뀌게 될 문자열", "바꿀 문자열")

# 문자열 나누기 split
a = "Life is too short"
a.split()      # ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(':')   # ['a', 'b', 'c', 'd']

# 02-3 리스트 자료형
# 리스트명 = [요소1, 요소2, 요소3, ...]
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]     # 리스트 자체를 요솟값으로 가짐

# 리스트의 인덱싱 indexing
a = [1, 2, 3]
a
a[0]         # 1 >> 리스트 a의 첫 번째 요솟값
a[0] + a[2]  # 4
a[-1]        # 3

a = [1, 2, 3, ['a', 'b', 'c']]
a[0]         # 1
a[-1]        # ['a', 'b', 'c']
a[3]         # ['a', 'b', 'c']

a[-1][0]     # 'a'
a[-1][2]     # 'c'

a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[2][2][0]   # 'Life' >> 삼중 리스트 인덱싱

# 리스트 슬라이싱 slicing
a = [1, 2, 3, 4, 5]
a[0:2]       # [1, 2]
a[:2]        # [1, 2]
a[2:]        # [3, 4, 5]

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
a[2:5]       # [3, ['a', 'b', 'c'], 4]
a[3][:2]     # ['a', 'b']

# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
a + b        #  [1, 2, 3, 4, 5, 6] : 더하기
a * 3        # [1, 2, 3, 1, 2, 3, 1, 2, 3] : 리스트 반복
len(a)       # 3 : 리스트 길이

# 리스트 값 수정과 삭제
a = [1, 2, 3]
a[2] = 4
a            # [1, 2, 4]

a = [1, 2, 3]
del a[1]
a            # [1, 3]
# del : 삭제 함수 

a = [1, 2, 3, 4, 5]
del a[2:]
a            # [1, 2] >> 슬라이싱 이용하여 삭제

# 리스트 관련 함수들
# 리스트에 요소 추가 append
a = [1, 2, 3]
a.append(4)
a           # [1, 2, 3, 4]

a.append([5,6])
a           # [1, 2, 3, 4, [5, 6]] >> 어떠한 자료형도 추가할 수 있음

# 리스트 정렬 sort
a = [1, 4, 3, 2]
a.sort()
a        # [1, 2, 3, 4]

a= ['a','c','b']
a.sort()
a        # ['a', 'b', 'c']

# 리스트 뒤집기 reverse
a = ['a', 'c', 'b']
a.reverse()
a        # ['b', 'c', 'a']

# 위치 반환 index
# index(x) : 리스트에 x 값이 있으면 x의 위치 값 반환
a = [1, 2, 3]
a.index(3)      # 2
a.index(1)      # 0
a.index(0)      # ValueError: 0 is not in list

# 리스트에 요소 삽입 insert
# insert(a,b) : 리스트의 a번째 위치에 b를 삽입
a = [1, 2, 3]
a.insert(0,4)
a           # [4, 1, 2, 3]

a.insert(3,5)
a           # [4, 1, 2, 5, 3]

# 리스트 요소 제거 remove
# remove(x) : 리스트에서 첫 번째로 나오는 x를 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a         # [1, 2, 1, 2, 3]
a.remove(3)
a         # [1, 2, 1, 2]

# 리스트 요소 끄집어내기 pop
# pop() : 리스트의 맨 마지막 요소를 돌려주고 그 요소 삭제
# pop(x) : 리스트의 x번째 요소를 돌려주고 그 요소 삭제
a = [1, 2, 3]
a.pop()     # 3 >> 맨 마지막 요소 끄집어내고
a           # [1, 2] >> 최종적으로 [1, 2] 만 남음

a = [1, 2, 3]
a.pop(1)    # 2 >> a[1]의 값을 끄집어내고
a           # [1, 3] >> 최종적으로 [1, 3] 만 남음

# 개수 세기 count
# count(x) : 리스트 안에 x가 몇 개 있는지 조사 후 개수 반환
a = [1, 2, 3, 1]
a.count(1)      # 2

# 리스트 확장 extend
# extend(x) : x에는 리스트만 올 수 있음
a = [1, 2, 3]
a.extend([4,5])
a          # [1, 2, 3, 4, 5]
b = [6, 7]
a.extend(b)
a          # [1, 2, 3, 4, 5, 6, 7]

 