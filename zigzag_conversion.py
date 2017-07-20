"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
											PAHNAPLSIIGYIR
"""
class Solution(object):
	#Not pass due to time limit
    def convert0(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows==1:
        	return s

        appeared_index = {}
        index = 0
        res = []
        prev_index_row = [0]
        while index < len(s):
            res.append(s[index])
            appeared_index[index] = True
            index += (2*numRows-2)
            prev_index_row.append(index)
            
            
        print prev_index_row
        row=1
        while row <= numRows and len(res) < len(s):
            prev_check_index_row = []
            for prev_index in prev_index_row:
                check = [prev_index-1, prev_index+1]
                for index in check:
                	prev_check_index_row.append(index)

                check = [item for item in check if item >=0 and item < len(s) 
                											and appeared_index.get(item, False) == False]

                for index in check:
                    res.append(s[index])
                    appeared_index[index] = True
                    
            
            prev_index_row = prev_check_index_row
            row+=1
        
        return ''.join(res)

    #118ms
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows==1:
            return s
        
        rows = ['']* numRows
        index = 0
        incre = 1
        row_index = 0
        while index < len(s):
            rows[row_index] += s[index]
            if row_index == 0:
                incre = 1
            elif row_index == numRows-1:
                incre = -1
            
            row_index += incre
            index +=1
        
        return ''.join(rows)
                    
                
            
if __name__ == '__main__':
	print Solution().convert('PAYPALISHIRING',3)
	# print Solution().convert('ABCDEF',5)
        
        