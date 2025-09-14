# Singly Link List Implementation in Python
class SinglyNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


# Making a Link List

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(5)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head.__str__())