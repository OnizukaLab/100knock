
def cipher(text):
    return ''.join([chr(219 - ord(x)) if x.islower() else x for x in text])


text = 'The quick brown fox jumps over the lazy dog'
encrypt = cipher(text)
print(encrypt)
print(cipher(encrypt))