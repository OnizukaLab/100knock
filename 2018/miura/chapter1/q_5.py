def n_gram(sequence, n):
	return [sequence[i:i+n] for i in range(len(sequence)-n+1)]

if __name__ == "__main__":
	s = "I am an NLPer"
	print(n_gram(s.split(" "), 2))
	print(n_gram(s, 2))
