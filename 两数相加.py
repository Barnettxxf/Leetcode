# -*- coding: utf-8 -*-

__author__ = 'barnett'


class Solution:
    """ the fastest solution """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        map = {}
        for i, values in enumerate(nums):
            if target - values not in map:
                map[values] = i
            else:
                return [map[target - values], i]


class MySolution:
    """ my own solution """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        index = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    index.append(i)
                    index.append(j)
                    return index
        return [-1, -1]
