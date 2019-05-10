import random

def typoglycemia(seq):
	return ' '.join([word if len(word) <= 4 else wordshuffle(word) for word in seq.split(' ')])	
	
	'''
	#まとも
	result = []
	for word in seq.split(' '):
		if len(word) <= 4:
			result.append(word)
		else:
			result.append(wordshuffle(word))
	return ' '.join(result)
	'''

def wordshuffle(word):
	result = [word[0]]
	result.extend(random.sample(word[1:-1],len(word[1:-1])))
	result.append(word[-1])
	return ''.join(result)

if __name__ == '__main__':
	s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
	print(typoglycemia(s))

