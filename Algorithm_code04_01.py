# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:30:53 2022

@author: jjunghu
"""

class Node() :              # Node라는 자료구조 만들기
    def __init__(self):
        self.data = None    # 아무것도 없는 것 빈 것 처음에 만들기
        self.link = None
        
        
node1 = Node()
node1.data = '다현'    

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5


# 재남 삽입
newNode = Node()
newNode.data = '재남'
newNode.link = node2.link   # 정연의 링크
node2.link = newNode        # 원래 정연의 링크에 재남 노드 지정


# 노드 삭제
node2.link = node3.link
del(node3)


# print(node1.data, end=' ')
# print(node1.link.data, end=' ')
# print(node1.link.link.data, end=' ')
# print(node1.link.link.link.data, end=' ')
# print(node1.link.link.link.link.data, end=' ')


current = node1    # current는 현재 작업하는 node
print(current.data, end=' ')
while current.link != None :
    current = current.link      # 현재 노드를 현재 노드의 링크가 가리키는 노드로 변경
    print(current.data, end=' ')
    
