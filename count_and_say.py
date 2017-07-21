'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        pos =1

        while pos != n:
        	tempres = ''
        	count = 0
        	for index in xrange(len(res)):
        		item = res[index]
        		if count == 0 or item == res[index-1]:
        			count +=1
        		elif item != res[index-1]:
        			tempres += str(count) + str(res[index-1])
        			count = 1

        	tempres += str(count) + str(res[-1])

        	pos +=1
        	res = tempres

        return res

    def countAndSay1(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(group)) + digit
                    for group, digit in re.findall(r'((.)\2*)', s))
    return s

        


if __name__ == '__main__':
	print Solution().countAndSay('3')
	print Solution().countAndSay('5')