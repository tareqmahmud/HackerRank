# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    # Write your code here
    node = SinglyLinkedListNode(node_data=data)

    if llist is None:
        llist = node
        return llist

    node.next = llist
    llist = node

    return llist
