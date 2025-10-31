# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(l1,l2):
            dummy = ListNode()
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            else:
                curr.next = l2
            return dummy.next
        if not lists:
            return None
        while len(lists) > 1:
            n = len(lists)
            mergelists = []
            for i in range(0, n, 2):
                l1 = lists[i]
                if i+1 < n:
                    l2 = lists[i+1]
                else:
                    l2 = None
                res = merge2Lists(l1,l2)
                mergelists.append(res)
            lists = mergelists
        return lists[0]