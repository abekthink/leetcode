#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

from typing import List

DIGIT_TO_CHAR_MAPPING = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                         "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


class Solution:
    # def letterCombinations(self, digits: str) -> List[str]:
    #     # DFS
    #     if not digits:
    #         return []
    #     res = []
    #     next_res = self.letterCombinations(digits[1:]) if len(digits) > 1 else []
    #     for char in DIGIT_TO_CHAR_MAPPING[digits[0]]:
    #         if next_res:
    #             for s in next_res:
    #                 res.append(char + s)
    #         else:
    #             res.append(char)
    #     return res

    def depth_first_search(self, digits: str, out: List[str], cur_str: str, length: int):
        if not digits:
            return
        for char in DIGIT_TO_CHAR_MAPPING[digits[0]]:
            if len(cur_str) + 1 == length:
                out.append(cur_str + char)
                continue
            self.depth_first_search(digits[1:], out, cur_str + char, length)

    def letterCombinations(self, digits: str) -> List[str]:
        # DFS
        res = []
        self.depth_first_search(digits, res, "", len(digits))
        return res


def main():
    s = Solution()
    print(s.letterCombinations("23"))


if __name__ == '__main__':
    main()
