'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
class Solution(object):
    def addBinary1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        mem = 0
        pos = 0
        res = ''
        lena = len(a)
        lenb = len(b)
        print 'lena=',lena,lenb
        while pos <= lena or pos <= lenb:
            ai = lena-pos-1 >=0 and a[lena-pos-1] or '0'
            bi = lenb-pos-1 >=0 and b[lenb-pos-1] or '0'
            if ai ==bi and ai=='0' and mem==0 and pos == max(lena, lenb):
            	print 'break',ai,bi
                break
            temp = int(ai) + int(bi)+ mem
            mem=0
            if temp >1:
                mem =1
                temp = temp-2
            res += str(temp)
            pos +=1
            print 'res=',res
        
        return res[::-1]

    #Better 
   	#Loop
    def addBinary(self, a, b):
        if not a:
            return b
        elif not b:
            return a
        
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary( self.addBinary(a[:-1], b[:-1]), '1') +'0'
        elif a[-1] =='0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'


    #Best
    #Convert binary string into integer by int(str,2)===>  a='11', int('11', 2) == 3
    def addBinary(self, a, b):
    	return bin(int(a,2) + int(b,2))[2:]
            
            

if __name__ == '__main__':
	print Solution().addBinary('100','110010')