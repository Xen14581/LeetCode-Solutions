class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = None
        pointer = None
        carry = 0

        while l1 is not None or l2 is not None:
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            node = ListNode(sum % 10)
            carry = sum // 10
            if pointer is None:
                pointer = head = node
            else:
                pointer.next = node
                pointer = pointer.next
        if carry > 0:
            pointer.next = ListNode(carry)
        return head