#!/usr/bin/python3
"""
Define a class node
"""
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
def __str__(self):
    result = []
    current = self._head
    while current is not None:
        result.append(str(current.data))
        current = current.next_node