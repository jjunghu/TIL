# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 19:45:26 2021

@author: jjunghu
"""

# 02-4. 튜플(tuple) 자료형
t1 = ()
t2 = (1,)            # 단지 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 함
t3 = (1, 2, 3)
t4 = 1, 2, 3         # 괄호 생략 가능
t5 = ('a', 'b', ('ab', 'cd'))
# 튜플의 항목 값은 변화가 불가능

t1 = (1, 2, 'a', 'b')
del t1[0]          # TypeError: 'tuple' object doesn't support item deletion
                   # 튜플의 요소는 삭제 불가능
                   
t1[0] = 'c'        # TypeError: 'tuple' object does not support item assignment
                   # 튜플의 요솟값 변경 불가능
                 
# 인덱싱 indexing
t1 = (1, 2, 'a', 'b')
t1[0]      # 1
t1[3]      # 'b'

# 슬라이싱 slicing
t1 = (1, 2, 'a', 'b')
t1[1:]     # (2, 'a', 'b')

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t1 + t2      # (1, 2, 'a', 'b', 3, 4) : 튜플 더하기
t2 * 3       # (3, 4, 3, 4, 3, 4)     : 튜플 곱하기(반복)
len(t1)      # 4  : 튜플의 길이 구하기

# 02-5. 딕셔너리(dictionary) 자료형
# Key와 Value를 한 쌍으로 갖는 자료형
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# Key에는 변하지 않는 값을 사용하고, 
# Value에는 변하는 값과 변하지 않는 값 모두 사용가능

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a = {1:'hi'}
a = {'a':[1, 2, 3]}

# 딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b'
a         # {1: 'a', 2: 'b'}
a['name'] = 'pey'
a         # {1: 'a', 2: 'b', 'name': 'pey'}
a[3] = [1, 2, 3]
a         # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리 요소 삭제
del a[1]
a         # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}
# del a[key] : Key에 해당하는 {key : value} 쌍이 삭제

# 딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey': 10, 'julliet': 99}
grade['pey']      # 10
grade['julliet']  # 99

a = {1:'a', 2:'b'}
a[1]      # 'a'
a[2]      # 'b'

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
dic['name']     # 'pey'
dic['phone']    # '0119993323'
dic['birth']    # '1118'

# 딕셔너리 관련 함수들
# Key 리스트 만들기 keys
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a.keys()      # dict_keys(['name', 'phone', 'birth'])

for k in a.keys():
    print(k)

# name
# phone
# birth

list(a.keys())      # ['name', 'phone', 'birth'] : 리스트로 변환

# Value 리스트 만들기 values
a.values()       # dict_values(['pey', '0119993323', '1118'])

# Key, Value 쌍 얻기 items
a.items()        # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

# Key, Value 쌍 모두 지우기 clear
a.clear()
a        # {}

# Key로 Value 얻기 get
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a.get('name')      # 'pey'
a.get('phone')     # '0119993323'

# 해당 Key가 딕셔너리 안에 있는지 조사 in
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
'name' in a       # True
'email' in a      # False

# 02-6. 집합 자료형
# 중복을 허용하지 않음
# 순서가 없음(Unordered
)
s1 = set([1, 2, 3])
s1      # {1, 2, 3}

s2 = set("Hello")
s2      # {'H', 'e', 'l', 'o'}

s = set()      # 비어 있는 집합 자료형

s1 = set([1, 2, 3])
l1 = list(s1)
l1      # [1, 2, 3]
l1[0]   # 1
t1 = tuple(s1)
t1      # (1, 2, 3)
t1[0]   # 1
# set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환 후 가능

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합 &
s1 & s2      # {4, 5, 6}  >> & : 교집합
s1.intersection(s2)       # {4, 5, 6}
s2.intersection(s1)       # {4, 5, 6}

# 합집합 |
s1 | s2      # {1, 2, 3, 4, 5, 6, 7, 8, 9}  >> | : 합집합
s1.union(s2)   # {1, 2, 3, 4, 5, 6, 7, 8, 9}
s2.union(s1)   # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합 -
s1 - s2      # {1, 2, 3}  >> - : 차집합
s2 - s1      # {7, 8, 9}
s1.difference(s2)   # {1, 2, 3}
s2.difference(s1)   # {7, 8, 9}

# 집합 자료형 관련 함수들
# 값 1개 추가하기 add
s1 = set([1, 2, 3])
s1.add(4)
s1       # {1, 2, 3, 4}

# 값 여러 개 추가하기 update
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1       # {1, 2, 3, 4, 5, 6}

# 특정 값 제거하기 remove
s1 = set([1, 2, 3])
s1.remove(2)
s1       # {1, 3}

# 02-7. 불(bool) 자료형
# 참(True), 거짓(False)
a = True
b = False
type(a)    # bool
type(b)    # bool

1 == 1     # True
2 > 1      # True
2 < 1      # False

# 자료형의 참과 거짓
# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있으면 "",[],(),{} : 거짓
# 비어있지 않으면 : 참

a = [1, 2, 3, 4]
while a:
    print(a.pop())
# 4
# 3
# 2
# 1

if []:
    print("참")
else:
    print("거짓")
# 거짓

if [11, 2, 3]:
    print("참")
else:
    print("거짓")
# 참

# 불 연산
bool('python')     # True
bool('')           # False
bool([1, 2, 3])    # True
bool([])           # False
bool(0)            # False
bool(3)            # True

# 02-8. 변수 : 자료형의 값을 저장하는 공간
# 변수를 만드는 여러가지 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
a = b = 'python'

a = 3
b = 5
a, b = b, a
a      # 5
b      # 3




    
    
    






