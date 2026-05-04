# Solution using set()

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        seen = set()
        currentA = headA
        while currentA:
            seen.add(currentA)
            currentA = currentA.next
        currentB = headB
        while currentB:
            if currentB in seen:
                return currentB
            currentB = currentB.next
        return None
    

# Two pointer Solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ap = headA
        bp = headB

        while ap != bp:
            ap = ap.next if ap else headB
            bp = bp.next if bp else headA
        return ap



    

