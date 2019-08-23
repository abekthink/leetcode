#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    #     i, m, n = 0, len(haystack), len(needle)
    #     while i < m - n + 1:
    #         j = 0
    #         while j < n and haystack[i + j] == needle[j]:
    #             j += 1
    #         if j == n:
    #             return i
    #         i += 1
    #     return -1 if needle else 0

    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1 if needle else 0


def main():
    s = Solution()
    print(s.strStr("hello", "ll"))
    print(s.strStr("aaaaa", "bba"))
    print(s.strStr("aaa", "aaaa"))
    print(s.strStr("hello", ""))
    print(s.strStr("", "ab"))


if __name__ == '__main__':
    main()
