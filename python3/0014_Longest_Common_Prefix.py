#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from python3 import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index, res, ln, stop = 0, "", len(strs), False
        while strs and not stop:
            for i in range(0, ln):
                if index >= len(strs[i]) or (i > 0 and strs[i - 1][index] != strs[i][index]):
                    stop = True
                    break
            if stop is False:
                res, index = res + strs[0][index], index + 1
        return res


def main():
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix([]))


if __name__ == '__main__':
    main()