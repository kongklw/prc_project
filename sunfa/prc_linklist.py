class Node(object):

    def __init__(self, item):
        self.item = item
        self.next = None


'''
链表依托
1、python 变量指向 定义一个变量，开辟一个空间，存储该变量的地址，而非该变量赋予的具体对象，比如并非存储指向的数值存储，函数存储，而是这些对象的地址。
2、游标和head指向。
'''


class SingleLinkList(object):

    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        count = 0
        cursor = self._head

        while cursor != None:
            count += 1
            cursor = cursor.next
        return count

    def travel(self):
        '''
        遍历链表
        :return:
        '''
        cursor = self._head

        while cursor != None:
            print('遍历', cursor.item)
            cursor = cursor.next

    def add(self, item):
        """头部添加元素"""

        '''
        节点的next 指向原来的head
        然后head 重新指向 现在的node
      
        '''
        node = Node(item)

        node.next = self._head
        self._head = node

        # if self.is_empty():
        #     self._head = node
        #
        # else:
        #     b = self._head
        #     self._head = node
        #     node.next = b

    def insert(self, position, item):

        node = Node(item)
        if self.is_empty():
            self._head = node

        elif self.length() <= position:
            # 如果插入位置大于链表长度，统一插在尾部
            self.append(item)

        else:

            # 找到哪个链表节点，和下一个节点。然后断开两个节点，重新加入该节点。
            if position == 0:
                self.add(item)
            else:
                cursor = self._head
                for i in range(position - 1):
                    cursor = cursor.next

                back_cursor = cursor.next

                cursor.next = node
                node.next = back_cursor

    def append(self, item):
        """尾部添加元素"""
        node = Node(item)

        '''
        先判断是否为空，空直接head指向item 不空，游标移动到一直为空的地方添加
        '''
        if self.is_empty():
            self._head = node
        else:
            cursor = self._head
            while cursor.next != None:
                print(cursor.next, cursor.item)
                cursor = cursor.next
            # 此时cursor 为none 了 没有next属性。
            cursor.next = node


if __name__ == '__main__':
    sll = SingleLinkList()
    sll.travel()
    sll.add(1)
    sll.add(2)
    sll.add(3)
    sll.add(4)
    sll.add(5)

    # sll.append(1)
    # sll.append(2)
    # sll.append(3)
    # sll.append(4)
    # sll.append(5)

    print(sll.is_empty())
    print(sll.length())
    sll.insert(1, 9)
    sll.travel()
