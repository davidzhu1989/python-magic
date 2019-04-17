#!/usr/bin/env python3
# coding=utf-8
__author__ = 'Boaz'
# @Time : 2019/4/14 20:04
# Two-sum.py

# Given an array of integers , return indices of the two numbers such they add
# up to a specific target
# Example:
# Given nums = [2, 7, 11, 15] target = 9
# Because nums[0] + nums[1] = 2 + 7 = 9
# return [0,1]


class Solution:
    def twosum(self, nums, target):
        """
        :param nums: list[int]
        :param target: int
        :return: list[int]
        """
        for i in nums:
            j = target - i
            start_index = nums.index(i)
            next_index = start_index + 1
            temp_nums = nums[next_index:]
            if j in temp_nums:
                # print(nums.index(i))
                # print(next_index + temp_nums.index(j))
                # list = [nums.index(i), next_index+temp_nums.index(j)]
                # return (nums.index(i), next_index + temp_nums.index(j))
                return [nums.index(i),next_index+temp_nums.index(j)]

    def twosum_plus(self, nums,target):
        hash_table = {}
        for i,num in enumerate(nums):
            if target-i in hash_table:
                return

if __name__ == '__main__':
    s = Solution()
    print(s.twosum([2, 7, 11, 15], 9))
