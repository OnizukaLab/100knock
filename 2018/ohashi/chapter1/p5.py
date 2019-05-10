def n_gram(text, n):
    return [' '.join(text[i:i+n]) for i in range(len(text) - n + 1)]

text = 'I am a NLPer'

print(n_gram(text.split(), 2))
print(n_gram([x for x in text.replace(' ', '')], 2))


