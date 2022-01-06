# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 16:05:39 2021

@author: jjunghu
"""

# 04장 프로그램의 입력과 출력
# 04-1 함수
# 함수: 입력값을 가지고 어떤 일을 수행한 다음에 그 결과물을 내어놓음

# def 함수명(매개변수):
#     <수행할 문장1>
#     <수행할 문장2>
#     ...

def add(a, b):
    return a + b

a = 3
b = 4
c = add(a,b)
print(c)      # 7

# 매개변수(parameter) vs 인수(arguments)
# 매개변수: 함수에 입력으로 전달된 값을 받는 변수
# 인수: 함수를 호출할 때 전달하는 입력값

def add(a, b):     # a, b는 매개변수
    return a + b

print(add(3,4))    # 3, 4는 인수

# 일반적인 함수
# 입력값이 있고 결과값이 있는 함수(대부분의 함수)
# def 함수이름(매개변수):
#     <수행할 문장>
#     ...
#     return 결과값

def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)      # 7

# 결과값을 받을 변수 =  함수이름(입력인수1, 입력인수2,...)

# 입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)     # Hi

# 결과값을 받을 변수 = 함수이름()

# 결과값이 없는 함수
def add(a, b):
    print('%d, %d의 합은 %d입니다.' %(a, b, a+b))
    
add(3, 4)     # 3, 4의 합은 7입니다.
# 함수이름(입력인수1, 입력인수2, ...)

# print문은 함수의 구성 요소 중 하나인 <수행할 문장>에 해당하는 부분
# 결과값은 당연히 없다. 결과값은 오직 return 명령어로만 돌려받을 수 있음

a = add(3, 4)
print(a)     # None


# 입력값도 결과값도 없는 함수
def say():
    print('Hi')
    
say()     # Hi
# 함수이름()

# 매개변수 지정하여 호출하기
def add(a, b):
    return a + b

result = add(a = 3, b = 7)
print(result)      # 10

result = add(b = 5, a = 3)
print(result)      # 8
# 매개변수를 지정하면 순서에 상관없이 사용가능

# 여러 개의 입력값을 받는 함수
# def 함수이름(*매개변수):
#     <수행할 문장>
#     ...

# ex) 여려 개의 입력값을 모두 더하는 함수
# add_many(1, 2)이면 3, add_many(1,2,3)이면 6, 
# add_many(1,2,3,4,5,6,7,8,9,10)이면 55를 돌려주는 함수

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

# args는 매개변수를 뜻하는 영어 단어 arguments의 약자이며 관례적으로 자주 사용
# 위에서 만든 add_many 함수는 입력값이 몇 개이든 상관없음
# *args처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아 튜플로 만들어줌
# add_many(1,2,3)처럼 이 함수를 쓰면 args는 (1,2,3)
# *args는 임의로 정한 변수 이름. *pey, *python처럼 아무 이름이나 써도 됨

result = add_many(1,2,3)
print(result)      # 6

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)      # 55

def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)     # 15

result = add_mul('mul', 1,2,3,4,5)
print(result)     # 120


# 키워드 파라미터 kwargs
# 매개변수 앞에 별 두개(**)를 붙임

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1)     # {'a': 1}
print_kwargs(name='foo', age=3)
# {'name': 'foo', 'age': 3}

# **kwargs처럼 매개변수 이름 앞에 **을 붙이면
# 매개변수 kwargs는 딕셔너리가 되고 
# 모든 key=value 형태의 결과값이 그 딕셔너리에 저장됨

def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
result      # (7, 12)

result1, result2 = add_and_mul(3,4)
result1     # 7
result2     # 12

def add_and_mul(a,b):
    return a+b
    return a*b

result = add_and_mul(2,3)
print(result)     # 5

# 함수는 return문을 만나는 순간 결과값을 돌려준 다음 함수를 빠져나감

# return의 또 다른 쓰임새
# 특별한 상황일 때 함수를 빠져나가고 싶다면 return 사용
def say_nick(nick):
    if nick == '바보':
        return
    print('나의 별명은 %s 입니다.' % nick)
    
say_nick('야호')     # 나의 별명은 야호 입니다.
say_nick('바보')     
# 입력값으로 '바보'라는 값이 들어오면 문자열을 출력하지 않고 함수를 즉시 빠져나감


# 매개변수에 초깃값 미리 설정
# 초기화시키고 싶은 매개변수는 항상 뒤쪽에 놓기

def say_myself(name, old, man=True):
    print('나의 이름은 %s 입니다.' % name)
    print('나이는 %d살 입니다.' % old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')
        
# man = True >> 초깃값을 설정 한 것

say_myself('박응용', 27)
say_myself('박응용', 27, True)
# 나의 이름은 박응용 입니다.
# 나이는 27살 입니다.
# 남자입니다.
# man이라는 변수에 입력값을 주지 않았지만 초깃값 True를 갖게 됨

say_myself('박응용', 27, False)
# 나의 이름은 박응용 입니다.
# 나이는 27살 입니다.
# 여자입니다.

a = 1
def vartest(a):
    a = a + 1
    
vartest(a)
print(a)

# 함수 안에서 새로 만든 매개변수는 함수 안에서만 사용하는 '함수만의 변수'!
# def vartest(a) 에서 입력값을 전달받는 매개변수 a는 함수 안에서만 사용하는 변수

def vartest(a):
    a = a + 1
    
vartest(3)
print(a)      # 1
# vartest(3)을 수행하면 vartest 함수 안에서 a는 4가 되지만
# 함수를 호출하고 난 뒤에 print(a) 문장은 오류 발생
# print(a) 에서 입력받아야하는 a 변수를 어디에서도 찾을 수가 없기 때문
# 함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐 함수 밖에서 사용되지 않음!!!


# 함수 안에서 함수 밖의 변수를 변경하는 방법
# ex) vartest라는 함수를 사용해서 함수 밖의 변수 a를 1만큼 증가시키는 방법
# 1. return 사용
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)       # 2

# 2. global 명령어 사용
# 가급적이면 사용하지 않는 것이 좋음
a = 1
def vartest():
    global a
    a = a + 1
    
vartest()
print(a)       # 2

# global a 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용한다는 뜻


# lambda
# 함수를 생성할 때 사용(def와 동일한 역할)
# 보통 함수를 한줄로 간결하게 만들 때 사용
# def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰임

# lambda 매개면수1, 매개변수2, ... : 매개변수를 이용한 표현식

add = lambda a, b: a+b
result = add(3, 4)
print(result)      # 7

def add(a, b):
    return a + b

result = add(3, 4)
print(result)      # 7


# 04-2 사용자 입력과 출력
# input
# input 은 입력되는 모든 것을 문자열로 취급

a = input()
a         # 'Life is too short, you need python'

# 프롬프트를 띄워서 사용자 입력 받기
# input('질문내용')

number = input('숫자를 입력하세요: ')
print(number)      # 3
# input은 입력되는 모든 것을 문자열로 취급하기에 number는 숫자가 아닌 문자
type(number)       # str


# print 자세히 알기
a = 123
print(a)    # 123

a = 'Python'
print(a)    # Python

a = [1, 2, 3]
print(a)    # [1, 2, 3]

# 큰 따옴표(")로 둘러싸인 문자열은 + 연산과 동일
print("life" "is" "too short")    # lifeistoo short
print("life"+"is"+"too short")    # lifeistoo short
print('life' 'is' 'too short')    # lifeistoo short

# 문자열 띄어쓰기는 콤마로
print('life', 'is', 'too short')  # life is too short

# 한 줄에 결괏값 출력
for i in range(10):
    print(i, end=' ')
# 0 1 2 3 4 5 6 7 8 9 
# 매개변수 end를 사용해 끝 문자 지정


# 04-3 파일 읽고 쓰기
# 파일 생성하기
# 파일 객체 = open(파일 이름, 파일 열기 모드)
f = open('새파일.txt','w')
f.close()

# r : 읽기모드 - 파일을 읽기만 할 때 사용
# w : 쓰기모드 - 파일에 내용을 쓸 때 사용
# a : 추가모드 - 파일의 마지막에 새로운 내용을 추가시킬 때 사용

f = open('C:/Users/jjunghu/Desktop/jjunghu/homework/새파일.txt','w')
f.close()

# 파일을 쓰기 모드로 열어 출력값 적기
f = open('C:/Users/jjunghu/Desktop/jjunghu/homework/새파일.txt','w')
for i in range(1, 11):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()

for i in range(1, 11):
    data = '%d번째 줄입니다.\n' % i
    print(data)

# 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
# readline 함수
f = open('C:/Users/jjunghu/Desktop/jjunghu/homework/새파일.txt', 'r')
line = f.readline()
print(line)
f.close()

# 1번째 줄입니다.
# 파일 읽기모드로 연 후 readline() 을 사용해서
# 파일의 첫 번째 줄을 읽어 출력하는 경우

f = open('C:/Users/jjunghu/Desktop/jjunghu/homework/새파일.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 1번째 줄입니다.

# 2번째 줄입니다.

# 3번째 줄입니다.

# 4번째 줄입니다.

# 5번째 줄입니다.

# 6번째 줄입니다.

# 7번째 줄입니다.

# 8번째 줄입니다.

# 9번째 줄입니다.

# 10번째 줄입니다.


# readlines 함수
f = open('C:/Users/jjunghu/Desktop/jjunghu/homework/새파일.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# 줄 바꿈(\n) 문자 제거하기
f = open('C:/Users/jjunghu/Desktop/jjunghu/homework/새파일.txt', 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()

# 1번째 줄입니다.
# 2번째 줄입니다.
# 3번째 줄입니다.
# 4번째 줄입니다.
# 5번째 줄입니다.
# 6번째 줄입니다.
# 7번째 줄입니다.
# 8번째 줄입니다.
# 9번째 줄입니다.
# 10번째 줄입니다.

# read 함수 
f = open('C:/Users/jjunghu/Desktop/jjunghu/homework/새파일.txt', 'r')
data = f.read()
print(data)
f.close()

# 1번째 줄입니다.
# 2번째 줄입니다.
# 3번째 줄입니다.
# 4번째 줄입니다.
# 5번째 줄입니다.
# 6번째 줄입니다.
# 7번째 줄입니다.
# 8번째 줄입니다.
# 9번째 줄입니다.
# 10번째 줄입니다.


# 파일에 새로운 내용 추가하기
f = open('C:/Users/jjunghu/Desktop/jjunghu/homework/새파일.txt', 'a')
for i in range(11, 20):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()

# with문과 함께 사용
with open('foo.txt','w') as f:
    f.write('Life is too short, you need python')
# with 블록을 벗어나는 순간 열린 파일 객체f가 자동으로 close





