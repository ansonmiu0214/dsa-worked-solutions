class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
    @classmethod
    def fromList(cls, list):
        if len(list) == 0:
            return None
        
        head, *tail = list
        return ListNode(head, cls.fromList(tail))

    def toList(self):
        if self.next is None:
            return [self.val]
        else:
            return [self.val, *self.next.toList()]