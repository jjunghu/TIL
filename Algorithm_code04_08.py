# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 14:01:39 2022

@author: jjunghu
"""

## 함수/클래스 선언부
class Node() :             
    def __init__(self):
        self.data = None    
        self.link = None
                
def printNode(start) : 
    current = start
    print(current.data, end=' ')
    while current.link != None :
        current = current.link
        print(current.data, end=' ')
    print( )

def insertNode(findData, insertData) :
    global memory, head, current, pre
    if head.data == findData :    # 첫 노드 앞에 삽입할 때
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # 사나 앞에 솔라를 삽입
    current = head
    while current.link != None :  # 없는 것을 찾을 수도 있으니
        pre = current             # pre를 놓치지 않기 위해 current 잡음
        current = current.link    # 다음 current로 이동
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current   # 솔라의 링크가 커런트를 가리킴
            pre.link = node       # pre의 링크가 솔라를 가리켜야함
            memory.append(node)
            return
    # 마지막에 추가할 때 (= 삽입할 이름이 존재하지 않을 때) 
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return       


def deleteNode(deleteData) :
    global memory, head, current, pre
    # 첫 노드 삭제
    if deleteData == head.data :
        current = head
        head = head.link    # 헤드를 삭제할 노드(다현노드)의 링크가 가리키던 정연 노드로 변경
        del(current)        # current가 다현노드이므로 current 삭제
        return
    # 첫 노드 외의 노드 삭제 
    current = head          # 헤드에서 작업시작! 삭제데이터를 처음위치부터 찾기위해
    while current.link != None : 
        pre = current       # 현재 노드를 pre로 저장
        current = current.link    # 현재 노드를 다음 노드로 이동
        if current.data == deleteData : 
            pre.link = current.link
            del(current)
            return
        
def findNode(findData) : 
    global memory, head, current, pre
    current = head
    if current.data == findData : 
        return current
    while current.link != None : 
        current = current.link
        if current.data == findData : 
            return current
    return Node()      # 빈 노드 변환



## 전역 변수
memory = []      # memory는 만든 애들을 담아 놓을 것
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']


## 메인 코드부
node = Node()   # 첫 노드
node.data = dataArray[0]
head = node                # 첫 번째 노드를 헤드(head)로 지정
memory.append(node)

for data in dataArray[1:] :     #['정연', '쯔위', '사나', '지효']
    pre = node        # node를 재사용하기 전에 pre가 바로 앞의 '다현'을 잡고 있는 상태
    node = Node()
    node.data = data
    pre.link = node       # 다현의 링크가 새로 만들어진 정연의 노드를 잡음
    memory.append(node)   # 부가적인 부분..
    
printNode(head)
    
insertNode('다현','화사')    
printNode(head)

insertNode('사나','솔라')    
printNode(head)

insertNode('재남','문별')    
printNode(head)

deleteNode('화사')
printNode(head)

deleteNode('쯔위')
printNode(head)

deleteNode('재남')
printNode(head)

fNode = findNode('다현')
print(fNode.data)
fNode = findNode('사나')
print(fNode.data)
