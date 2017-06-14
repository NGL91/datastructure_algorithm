'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(1, rowIndex+1):
            row =map(lambda x, y: x+y, row +[0], [0]+ row)
            
        
        return row

if __name__ == '__main__':
    print Solution().getRow(2)