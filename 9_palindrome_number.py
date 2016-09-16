'''
Determine whether an integer is a palindrome. Do this without extra space.

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

    def isPalindrome2(self, x):
        '''
        If we dont want extra spaces to save the integer, we can divide the number by 10 to get both
        reminder and result and compare the higgest digit and the reminder.
        Repeat the same step until end
        '''

        if x < 0:
            return False
        div = 1
        while x/div >= 10:
            div = div * 10
            
        while x:
            left = x / div
            right = x % 10
            
            if left != right:
                return False
            x = ( x % div ) / 10
            div = div / 100
        return True
