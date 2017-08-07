'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        len1 = len(num1)
        len2 = len(num2)
        mem = 0
        for i in xrange(len(num1)):
            for j in xrange(len2):
				item_first = num1[len1-i-1]
				item_mul = num2[len2-j-1]
				temp_mul = (ord(item_first)-ord('0')) * (ord(item_mul)- ord('0'))
				print  '\nitem==',item_first,item_mul
				temp_mul = str(temp_mul)
				pos = 0
				
				for k in range(i+j, i+j+len(temp_mul)):
					# print k
					# print mem
					# print temp_mul[len(temp_mul)-1-k+i+j]

					new_item = int(len(res) > k and res[k] or 0) + int(temp_mul[len(temp_mul)-1-k+i+j]) + mem
					
					print ' new_item=',new_item, len(res) > k and res[k] or 0, mem
					mem = 0
					if new_item >=10:
					    mem = new_item/10
					    new_item = new_item%10
					print 'mem=',mem, new_item
					if len(res) > k:
						res[k] = new_item
					else:
						res.append(new_item)
                        
        print res
                
if __name__ == '__main__':
	print Solution().multiply('123','456')