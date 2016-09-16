'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''

'''
The idea is below:
input: [1,2,3,4,5]
                |
              | |
            | | |
          | | | |
        | | | | |
index:  0 1 2 3 4
with line 0 and line 4:  
    Water area is (line4_index - line0_index) * (min_height(line4, line0)) = (4-0) * 1 = 4
with line 1 and line 4:  
    Water area is (4-1) * 2 = 6
with line 2 and line 4:
    Water area is (4-2) * 3 = 6
and keep going ...

We can shift left to the right by 1 each time until the left height is greater than the right height.
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                water = height[left] * (right - left)
                left += 1
            else:
                water = height[right] * (right - left)
                right -= 1
            ans = max(ans, water) 
        return ans