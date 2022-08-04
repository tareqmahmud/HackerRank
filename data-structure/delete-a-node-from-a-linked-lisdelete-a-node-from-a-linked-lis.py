#
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    if position == 0:
        return llist.next

    # Write your code here
    index = 0
    current_node = llist

    while current_node:
        if (index + 1) == position:
            current_node.next = current_node.next.next
            break
        index += 1
        current_node = current_node.next

    return llist
