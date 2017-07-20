'''
Write a function to find the longest common prefix string amongst an array of strings.

'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ''
        length = len(strs)
        if length <2:
            return strs and strs[0] or ''
        
        for i in xrange(len(strs[0])):
            for item in strs[1:]:
                if i>= len(item) or strs[0][i] != item[i]:
                    return strs[0][:i]
        
        return strs[0]
            
                    
if __name__ == '__main__':
    print Solution().longestCommonPrefix(['c','c'])
    print Solution().longestCommonPrefix(["abab","aba","abc"])
        