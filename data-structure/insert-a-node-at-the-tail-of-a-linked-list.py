# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(node_data=data)

    # If head is empty then
    if head is None:
        head = node
        return head

    current_node = head

    while current_node is not None:
        if current_node.next is None:
            current_node.next = node
            return head
        else:
            current_node = current_node.next

    return head
