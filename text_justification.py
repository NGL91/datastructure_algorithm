"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
"""
class Solution(object):
	def fullJustify_old(self, words, maxWidth):
		"""
		:type words: List[str]
		:type maxWidth: int
		:rtype: List[str]
		"""
		res = []
		index = 0
		length_words = len(words)
		while index < length_words:
			temp_line = []
			temp_len = -1
			while index < length_words and temp_len <= maxWidth and  temp_len + 1+ len(words[index]) <= maxWidth:
				temp_line.append(words[index])
				temp_len += 1 + len(words[index])
				index +=1

			num_of_word = len(temp_line)
			gap = maxWidth - temp_len
			incre_gap = 1
			if num_of_word >1:
				incre_gap = gap/(num_of_word -1) +1
			lazy_gap = gap - (incre_gap -1) * (num_of_word-1)
			line = ''
			for i, item in enumerate(temp_line):
				if i != len(temp_line)-1:
					line += item + ' '* incre_gap
				else:
					line += item + ' '* lazy_gap
			res.append(line)

		return res

	def fullJustify_new(self, words, maxWidth): 
		res = []
		num_of_letters = 0
		line = []
		for w in words:
			if num_of_letters + len(w) + len(line) >= maxWidth:
				for i in range(maxWidth-num_of_letters-len(w)):
					line[i% (len(line)-1 or 1)] += ' '
 				res.append(''.join(line))
				line = []
				num_of_letters = 0

			line.append(w)
			num_of_letters+= len(w)

		res.append(' '.join(line))
		return res




	#correct more
	#user loop to insert space after word in line
	def fullJustify(self, words, maxWidth):
	    res, cur, num_of_letters = [], [], 0
	    for w in words:
	        if num_of_letters + len(w) + len(cur) > maxWidth:
	            for i in range(maxWidth - num_of_letters):
	                cur[i%(len(cur)-1 or 1)] += ' '
	            res.append(''.join(cur))
	            cur, num_of_letters = [], 0
	        cur += [w]
	        num_of_letters += len(w)
	    return res + [' '.join(cur).ljust(maxWidth)]






if __name__ == '__main__':
	print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
	# print Solution().fullJustify([""], 0)
	print Solution().fullJustify(["What","must","be","shall","be."], 12)