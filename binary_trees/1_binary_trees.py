#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def print_elements(self):
        print("hello")
        """print(self.data)"""
        if self.left:
            self.left.print_elements()
        """print(self.data)"""
        if self.right:
            self.right.print_elements()

        print(self.data)


root = Node(1)
number2 = Node(2)
number3 = Node(3)
number4 = Node(4)
number5 = Node(5)
number6 = Node(6)
number7 = Node(7)

root.left = number2
root.right = number3
number2.left = number4
number2.right = number5
number3.left = number6
number3.right = number7

root.print_elements()
"""
            1
           / \
          2   3
         / \ / \
        4  5 6  7 """
