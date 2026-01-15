import LinkedList_Practise
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverselinkedlist(head):
        prev = None
        current = head

        while current:
            n = current.next
            current.next = prev
            prev = current
            current = n
        LinkedList_Practise.printLinkedList(prev)
        return prev

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

print("After reversing a linked list")

reverselinkedlist(node1)

