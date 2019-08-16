#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        mid_len = len(s) >> 1
        for i in range(mid_len):
            if s[i] != s[-(i + 1)]:
                return False
        return True


def main():
    s = Solution()
    print(s.isPalindrome(0))
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))


if __name__ == '__main__':
    main()
