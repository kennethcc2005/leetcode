'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert('abcdefghi', 4) ->

a     g 
b   f h 
c e
d 

return: agbfhced
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == '':
            return s
        ans = []
        extra = numRows - 2
        groups = len(s)/(2*numRows-2)
        for i in xrange(numRows):
            for ix,v in enumerate(s):
                if ix % (2*numRows-2) == i:
                    ans.append(v)
                elif ix % (2*numRows-2) == 2*numRows-2 - i:
                    ans.append(v)
        return ''.join(ans)
