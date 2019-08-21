#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: abekthink

import re
import json
import bisect
import heapq

from math import pow
from typing import List
from collections import defaultdict


# Playground for linked-list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def listToListNode(ls):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in ls:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)
    return listToListNode(numbers)


def stringToListNodeArray(input):
    # Generate list from the input
    lists = json.loads(input)

    # Now convert that two dimension list into linked list array
    res = []
    for ls in lists:
        res.append(listToListNode(ls))
    return res


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end='')
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")
