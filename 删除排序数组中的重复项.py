# -*- coding: utf-8 -*-

__author__ = 'barnett'


class Solution:
    """ the fastest solution """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i=i+1
        return i+1

class MySolution:
    """ my own solution """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        record = 0
        i = 0
        j = 1
        while i < len(nums):
            while j < len(nums):
                if nums[i] != nums[j]:
                    nums[i + 1] = nums[j]
                    record = i + 2
                    break
                j += 1
            i += 1
        if record == 0:
            return 1
        return record