#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     p1, p2 = l1, l2
    #     head, tail = None, None
    #     carry = 0
    #     while p1 or p2:
    #         if p1:
    #             num1 = p1.val
    #             p1 = p1.next
    #         else:
    #             num1 = 0
    #             p1 = None
    #
    #         if p2:
    #             num2 = p2.val
    #             p2 = p2.next
    #         else:
    #             num2 = 0
    #             p2 = None
    #
    #         num3 = num1 + num2 + carry
    #         if num3 >= 10:
    #             carry = 1
    #             num3 = num3 - 10
    #         else:
    #             carry = 0
    #
    #         node = ListNode(num3)
    #         if head is None:
    #             head = node
    #             tail = node
    #         else:
    #             tail.next = node
    #             tail = tail.next
    #     if carry > 0:
    #         tail.next = ListNode(carry)
    #     return head

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode(0)
        carry = 0
        while l1 or l2:
            num = carry
            if l1:
                num += l1.val
                l1 = l1.next

            if l2:
                num += l2.val
                l2 = l2.next

            tail.next = ListNode(num % 10)
            tail = tail.next
            carry = num // 10

        if carry > 0:
            tail.next = ListNode(carry)

        return head.next
