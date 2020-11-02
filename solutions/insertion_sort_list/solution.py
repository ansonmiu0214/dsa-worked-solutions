from ..utils import ListNode

def insertionSortList(head: ListNode, result: ListNode = None) -> ListNode:
    """Sort linked list represented by 'head' using insertion sort,
    and return new sorted linked list."""
    
    if head is None:
        return result
    
    tail = head.next
    node = ListNode(head.val)
    
    prev = None
    curr = result
    while curr is not None and node.val > curr.val:
        prev = curr
        curr = curr.next
    
    if prev is None:
        node.next = curr
        return insertionSortList(tail, node)
    else:
        prev.next = node
        node.next = curr
        return insertionSortList(tail, result)