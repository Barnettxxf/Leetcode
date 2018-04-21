# -*- coding: utf-8 -*-

__author__ = 'barnett'


class Solution:
    """ the fastest solution """

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0 and x == int(str(x)[::-1]):
            return True
        else:
            return False


class MySolution:
    """ my own solution """

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        newx = x
        result = 0
        while newx != 0:
            tail = newx % 10
            result = result * 10 + tail
            newx = newx // 10
        if result == x:
            return True
        return False
