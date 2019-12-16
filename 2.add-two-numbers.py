#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Accepted
# 1563/1563 cases passed (44 ms)
# Your runtime beats 99.83 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        current = head
        carry = 0
        while l1 or l2 or carry:
            carry,currval = divmod(((l1.val if l1 else 0)+(l2.val if l2 else 0)+carry), 10)
            current.next = ListNode(currval)
            current = current.next
            l1 = l1.next if l1 else None
            l2= l2.next if l2 else None
        return head.next

# @lc code=end

