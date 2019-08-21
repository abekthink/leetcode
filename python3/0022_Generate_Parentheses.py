#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from python3 import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def depth_first_search(comb_str: str, left: int, right: int):
            if left == right == 0:
                res.append(comb_str)
                return
            if left > 0:
                depth_first_search(comb_str + '(', left - 1, right)
            if right > left:
                depth_first_search(comb_str + ')', left, right - 1)

        depth_first_search("", n, n)
        return res


def main():
    s = Solution()
    print(s.generateParenthesis(3))


if __name__ == '__main__':
    main()
