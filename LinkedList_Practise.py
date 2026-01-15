
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

def printLinkedList(head):
    while head:
        print(head.value)
        head = head.next

printLinkedList(node1)

def searchNode(head, value):
    while head:
        if head.value == value:
            print("True")
            return head
        head = head.next

    print("False")

def insertNodeAtStart(head, value):
    node = Node(value)
    node.next = head
    head = node
    printLinkedList(head)
print("After Inserting Node at Start:")
insertNodeAtStart(node1, 0)

def insertNodeAtEnd(head, value):


    node = Node(value)
    if head is None:
        return node
    temp = head
    while head.next:
        head = head.next

    head.next= node
    head = temp
    printLinkedList(head)

print("After Inserting Node at End:")
insertNodeAtEnd(node1, 5)

def insertNodeAtSpecificPos(head, value,position):
    node = Node(value)

    if position == 1:
        node.next = head
        return node
    currentNode = head
    for i in range(1,position-1):
        if currentNode is None:
            printLinkedList(head)
            return head
        currentNode = currentNode.next
    if currentNode is None:
        printLinkedList(head)
        return head
    node.next = currentNode.next
    currentNode.next = node
    printLinkedList(head)

print("After Inserting Node at Specific Position:")
insertNodeAtSpecificPos(node1, 10, 8)

def deleteNodeAtStart(head):

    head = head.next
    printLinkedList(head)

print("After Deleting Node at Start:")
deleteNodeAtStart(node1)

def deleteNodeAtEnd(head):
    currentNode = head

    while currentNode.next.next:
        currentNode = currentNode.next

    currentNode.next = None
    printLinkedList(head)

print("After Deleting Node at End:")
deleteNodeAtEnd(node1)


