def cipher(string):
    return "".join(map(lambda c: chr(219 - ord(c)) if ord(c) in range(ord('a'), ord('z') + 1) else c, string))


string = "abcdEFGH"
print(cipher(string))
print(cipher(cipher(string)))
