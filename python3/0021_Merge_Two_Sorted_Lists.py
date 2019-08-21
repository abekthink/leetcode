#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from python3 import ListNode, stringToListNode, listNodeToString


class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     tail = dummy = ListNode(0)
    #     while l1 or l2:
    #         if l2 is None or (l1 and l1.val < l2.val):
    #             tail.next, l1 = l1, l1.next
    #         else:
    #             tail.next, l2 = l2, l2.next
    #         tail = tail.next
    #     return dummy.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tail = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next


def main():
    s = Solution()
    print(listNodeToString(s.mergeTwoLists(stringToListNode('[1, 2, 4]'), stringToListNode('[1, 3, 4]'))))


if __name__ == '__main__':
    main()
