from p41 import Chunk, get_chunks

def get_path(s, m, morph=False):
    ret = [m.get_sentence() if not morph else m]
    index = s.index(m)
    while index != -1:
        m = s[m.dst]
        ret.append(m.get_sentence() if not morph else m)
        index = m.dst

    return ret


if __name__ == '__main__':
    text = list(filter([].__ne__, get_chunks()))


    index = 23
    list_ = [x for x in text[index] if '名詞' in x.get_pos_list()]

    [print(' -> '.join(get_path(text[index], l))) for l in list_]

