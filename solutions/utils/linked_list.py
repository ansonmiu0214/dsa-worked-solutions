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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False

        return self.val == other.val and self.next == other.next

    def __repr__(self):
        return f'ListNode.fromList({self.toList()})'

    def __str__(self):
        return f'[{",".join(map(str, self.toList()))}]'