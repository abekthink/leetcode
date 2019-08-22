#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


from python3 import ListNode, listNodeToString, listToListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy, dummy.next = self, head
        while dummy:
            cur, group = dummy, []
            while len(group) < k and cur.next:
                cur = cur.next
                group.append(cur)
            if len(group) != k: break
            nx = cur.next
            for node in group[::-1]:
                dummy.next = dummy = node
            dummy.next = nx
        return self.next


def main():
    s = Solution()
    print(listNodeToString(s.reverseKGroup(listToListNode([1, 2, 3, 4, 5]), 1)))
    print(listNodeToString(s.reverseKGroup(listToListNode([1, 2, 3, 4, 5]), 2)))
    print(listNodeToString(s.reverseKGroup(listToListNode([1, 2, 3, 4, 5]), 3)))

if __name__ == '__main__':
    main()
