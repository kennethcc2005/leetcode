'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

from collections import defaultdict,Counter
'''
There are different approaches to this problem and below are some of the solutions.
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        Although this solution only use for loop once. 'in' operator uses O(n) time in list operation
        The run time for this one is max at O(n^2)
        '''
        for i,v in enumerate(nums):
            c = target - v
            if c in nums[i+1:]:
                idx_2 = nums[i+1:].index(c)+i+1
                return [i,idx_2]

    def twoSum2(self, nums, target):
        '''
        The second solution only use for loop twice. 
        1st created the dictionary for each key using defaultdict list.
        2nd create target  'in' operator uses O(n) time in list operation
        The run time for this one is max at O(2n)
        '''
        new_dict = defaultdict(list)
        for i,v in enumerate(nums):
            new_dict[v].append(i)
        for i,v in enumerate(nums):
            c = target - v
            if c in new_dict:
                if len(new_dict[c]) == 2:
                    return new_dict[c]
                elif new_dict[c][0] != i:
                    return [i, new_dict[c][0]]

    def twoSum3(self, nums, target):
        '''
        The third solution is using Counter to find solution with duplicated number
        This solutions compared two defaultdict and has similar run time as solution2 with O(3n)
        '''
        a = defaultdict()
        b = defaultdict()
        ans = {}
        ans_ix = []
        c = Counter(nums)
        for i,v in enumerate(nums):
            a[v] = target - v
            b[target-v] = v
        for i, v in a.iteritems():
            if i in b:
                if i != b[i]:
                    ans[i] = True
                    ans[b[i]] = True
                    continue
                if i == b[i]:
                    if c[i] == 2:
                        ans[i] = True
                    continue
        for i,v in enumerate(nums):
            if v in ans:
                ans_ix.append(i)
        return ans_ix
        