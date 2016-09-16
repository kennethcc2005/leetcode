
'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

'''
Since in python, we don't need to worry about overflows. We still want to make sure a is not greater than 
a 32-bit integer in order to avoid errors for the submission.  
There are several ways to handle this case, and below is the simplest but not the fastest way.
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            a = str(abs(x))[::-1]
            a = int(a)
            if a > 2**31:
                return 0
            return -a
        else:
            a = str(x)[::-1]
            a = int(a)
            if a >2**31:
                return 0
            return a