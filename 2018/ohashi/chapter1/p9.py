import random

def shuffle(text):
    list_ = text.split()
    for i in range(len(list_)):
        if len(list_[i]) >= 4:
            tmp = list(list_[i][1:-1])
            random.shuffle(tmp)
            list_[i] = list_[i][0] + ''.join(tmp) + list_[i][-1]

    return ' '.join(list_)


text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(shuffle(text))