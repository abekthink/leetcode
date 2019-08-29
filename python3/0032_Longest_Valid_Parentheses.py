#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink


class Solution:
    # def longestValidParentheses(self, s: str) -> int:
    #     length, stack = len(s), []
    #     for i in range(length):
    #         if s[i] == '(':
    #             stack.append(i)
    #         elif stack and s[stack[-1]] == '(':
    #             stack.pop()
    #         else:
    #             stack.append(i)
    #     stack = [-1] + stack + [length]
    #     ans = 0
    #     for i in range(len(stack) - 1):
    #         ans = max(ans, stack[i + 1] - stack[i] - 1)
    #     return ans

    def longestValidParentheses(self, s: str) -> int:
        """
        Dynamic Programming
        dp[i]: the longest length valid parentheses which ends with s[i-1]
        """
        length = len(s)
        if length < 2:
            return 0

        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == '(':
                dp[i] = 0
            else:
                pre_len = dp[i - 1]
                j = i - 1 - pre_len
                if j < 0 or s[j] == ')':
                    dp[i] = 0
                    continue
                if j - 1 > 0:
                    dp[i] = dp[i - 1] + 2 + dp[j - 1]
                else:
                    dp[i] = dp[i - 1] + 2
        return max(dp)


def main():
    s = Solution()
    print(s.longestValidParentheses("(()"))
    print(s.longestValidParentheses(")()())"))
    print(s.longestValidParentheses("(()(()"))
    print(s.longestValidParentheses("((()(()"))
    print(s.longestValidParentheses("((((()())()())))"))
    print(s.longestValidParentheses("((((()()"))
    print(s.longestValidParentheses("((((()())()()))()(()))"))
    print(s.longestValidParentheses(")(((((()())()()))()(()))("))


if __name__ == '__main__':
    main()
