#
# Complete the 'reversePrint' function below.
#
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reversePrint(llist):
    # Write your code here
    current_node = llist
    converted_list = []
    while current_node:
        converted_list.append(current_node.data)
        current_node = current_node.next
    converted_list.reverse()
    for i in range(len(converted_list)):
        print(converted_list[i])
