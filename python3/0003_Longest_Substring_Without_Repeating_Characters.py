#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        char_index = defaultdict(int)
        left = res = 0
        for i in range(len(s)):
            left = max(left, char_index[s[i]])
            res = max(res, i - left + 1)
            char_index[s[i]] = i + 1
        return res


def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))


if __name__ == '__main__':
    main()
