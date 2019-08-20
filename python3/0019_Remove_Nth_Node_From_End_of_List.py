#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        array = []
        node = new_head
        while node is not None:
            array.append(node)
            node = node.next

        if len(array) == 2:
            return None
        array[-(n + 1)].next = array[-(n - 1)] if n > 1 else None
        return new_head.next
