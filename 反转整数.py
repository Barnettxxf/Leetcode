# -*- coding: utf-8 -*-

__author__ = 'barnett'


class Solution:
    """ the fastest solution """

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        newx = abs(x)
        maxminrange = 2 ** 31
        while (newx != 0):
            tail = newx % 10
            result = result * 10 + tail
            newx = newx // 10
        if result > maxminrange or result < -maxminrange:
            return 0
        else:
            if x > 0:
                return result
            else:
                return -result


class MySolution:
    """ my own Solution"""

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if str(x).startswith('-'):
            negative = True
            x1 = str(x)[1:]
        else:
            x1 = str(x)

        x1 = reversed(x1)
        x1 = int(''.join(x1))
        if x1 > 2 ** 31:
            return 0
        else:
            if negative:
                return x1 * -1
            return x1
