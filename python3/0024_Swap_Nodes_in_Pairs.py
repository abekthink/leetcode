#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from python3 import ListNode, listNodeToString, listToListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = tail = ListNode(0)
        dummy.next = head
        while tail.next and tail.next.next:
            first = tail.next
            second = first.next
            third = second.next
            tail.next, second.next, first.next, tail = second, first, third, first
        return dummy.next

    # def swapPairs(self, head: ListNode) -> ListNode:
    #     dummy, dummy.next = self, head
    #     while dummy.next and dummy.next.next:
    #         first = dummy.next
    #         second = first.next
    #         third = second.next
    #         dummy.next, second.next, first.next, dummy = second, first, third, first
    #     return self.next


def main():
    s = Solution()
    print(listNodeToString(s.swapPairs(listToListNode([1, 2, 3, 4]))))
    print(listNodeToString(s.swapPairs(listToListNode([1, 2, 3, 4, 5]))))
    print(listNodeToString(s.swapPairs(listToListNode([1]))))

if __name__ == '__main__':
    main()
