#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from python3 import ListNode


class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     new_head = ListNode(0)
    #     new_head.next = head
    #     array = []
    #     node = new_head
    #     while node is not None:
    #         array.append(node)
    #         node = node.next
    #
    #     if len(array) == 2:
    #         return None
    #     array[-(n + 1)].next = array[-(n - 1)] if n > 1 else None
    #     return new_head.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head

        slow, fast = new_head, new_head
        for i in range(n):
            fast = fast.next

        while fast.next is not None:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return new_head.next

