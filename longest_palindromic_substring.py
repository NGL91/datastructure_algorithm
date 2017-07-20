'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''

class Solution(object):
	#only beat 20%
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res = []
        for index, item in enumerate(s):
            j = len(s)-1
            while j >= index:
                if s[j] ==  item and s[index:j+1] == s[index:j+1][::-1] and (not res or len(s[index:j+1]) > res[0]):
                    res = [len(s[index:j+1]), s[index:j+1]]
                    break
                j-=1
            if j == len(s)-1:
                break
        
        return res and res[1]

if __name__ == '__main__':
	print Solution().longestPalindrome('babab')