# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 and not lists:
            return None

        while len(lists) > 1:
            mergeLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = None
                if i+1 <len(lists):
                    l2 = lists[i+1]
                mergeLists.append(self.merge2Lists(l1,l2))
            lists = mergeLists
        return lists[0]

    def merge2Lists(self, l1,l2):
        dummy = ListNode(-1)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next