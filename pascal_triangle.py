'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        res = [[1]]
        if numRows == 0:
            return []
        
        elif numRows==1:
            return [[1]]
        
        for i in range(2, numRows+1):
            cal_row = res[i-2]
            cal_row = [0] + cal_row + [0]
            new_row = []
            for j in range(1, len(cal_row)):
                new_row.append(cal_row[j]+ cal_row[j-1])
            res.append(new_row)
        
        return res

    def generate1(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
                


if __name__ == '__main__':
    print Solution().generate(5)
    print Solution().getRow(5)