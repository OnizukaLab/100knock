
def cipher(seq):
	return ''.join([chr(219-ord(char)) if ord('a') <= ord(char) <= ord('z') else char for char in seq])

	'''
	#等価
	result = []
	for char in seq:
		code = ord(char)
		if ord('a') <= code <= ord('z'):
			result.append(chr(219-code))
		else:
			result.append(char)
	return ''.join(result)
	'''

if __name__ == '__main__':
	s = 'Girls Like Robots.'
	print(cipher(s))
	print(cipher(cipher(s)))
