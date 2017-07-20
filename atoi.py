'''
Implement atoi to convert a string to an integer.

'''
class Solution(object):
	def myAtoi(self, stri):
		"""
		:type str: str
		:rtype: int
		"""
		INT_MAX =  2147483647
		INT_MIN = -2147483648
		stri = stri.strip()
		if not stri:
			return 0

		sign=1
		if stri[0] == '-':
			sign = -1

		if stri[0] in ['-','+']:
			stri = stri[1:]

		stri = stri.split('.')[0]
		res = 0
		length = len(stri)
		index=0
		print 'stri=',stri
		while index < length and (ord(stri[index]) >= ord('0')) and (ord(stri[index]) <= ord('9')):
			if res > (INT_MAX - (ord(stri[index])-ord('0')))/10:
				return INT_MAX if sign>0 else INT_MIN
			item = stri[index]
			res = res*10 + (ord(stri[index])-ord('0'))
			index +=1

		return sign* res



if __name__ == '__main__':
	# print Solution().myAtoi('12312')
	print Solution().myAtoi("  -0012a42")
	print Solution().myAtoi('2147483648')
	# print Solution().convert('ABCDEF',5)
        
        