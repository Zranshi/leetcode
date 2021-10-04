#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/05 07:39
# @Author   : Ranshi
# @File     : main.py


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.pk = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.pk is None:
            self.pk = self.iter.next()
        return self.pk

    def next(self):
        """
        :rtype: int
        """
        if self.pk is not None:
            val = self.pk
            self.pk = None
            return val
        return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pk is not None or self.iter.hasNext()
