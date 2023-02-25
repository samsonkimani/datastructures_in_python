class Node:

    def __inti__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertAfter(self, prev_node, new_data):

        if prev_node == None:
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
