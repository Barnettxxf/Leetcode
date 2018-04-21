# -*- coding: utf-8 -*-

__author__ = 'barnett'

"""
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表
示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
"""


class Solution:
    """ the fastest solution """
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        pre = 0
        length = len(s)
        i = length - 1
        while i >= 0:
            value = roman_dict[s[i]]
            if value >= pre:
                result += value
            else:
                result -= value
            pre = value
            i -= 1
        return result


class MySolution:
    """ my own solution """
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanChar = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        i = 0
        result = 0
        sl = len(s)
        while i < sl:
            if s[i] == 'I' and i + 1 < sl and s[i + 1] in ['V', 'X']:
                result += romanChar[s[i] + s[i + 1]]
                i += 2
            elif s[i] == 'X' and i + 1 < sl and s[i + 1] in ['L', 'C']:
                result += romanChar[s[i] + s[i + 1]]
                i += 2
            elif s[i] == 'C' and i + 1 < sl and s[i + 1] in ['D', 'M']:
                result += romanChar[s[i] + s[i + 1]]
                i += 2
            else:
                result += romanChar[s[i]]
                i += 1
        return result


if __name__ == '__main__':
    t = MySolution()
    print(t.romanToInt('MCMXCIV'))
