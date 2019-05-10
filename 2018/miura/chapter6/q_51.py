from q_50 import *

sentences_word = [[re.sub(r'[.,()"\']', '', word) for word in sentence.split()] for sentence in sentences]

if __name__ == '__main__':
    for sentence in sentences_word:
        print('\n'.join(sentence)+'\n')
