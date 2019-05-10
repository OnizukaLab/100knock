from q_41 import *

#i -> 根 のパスのリストを返す
def dst_list(i, chunks):
    result = [i]
    dst = chunks[i].dst
    while dst != -1:
        result.append(dst)
        dst = chunks[dst].dst
    return result

def extract_path(chunks):
    for i in range(len(chunks)):
        if not chunks[i].in_noun(): continue
        for j in range(i+1,len(chunks)):
            if not chunks[j].in_noun(): continue

            #i -> 根 のパス
            i_list = dst_list(i, chunks)

            #i -> 根 の間にjがあったとき
            if j in i_list:
                for n in i_list:
                    if n == i:
                        print(chunks[i].noun_replace('X'), end='')
                    elif n == j:
                        print(' -> ' + chunks[j].noun_replace('Y'), end='')
                        break
                    else: print(' -> ' + chunks[n].surface(), end='')
                print('')
                continue

            #ないとき
            #j -> 根 のパス
            j_list = dst_list(j, chunks)
            #共通の文節k
            k = min(set(i_list) & set(j_list))
            #i -> kの手前まで
            for n in i_list:
                if n == i:
                    print(chunks[i].noun_replace('X'), end='')
                elif n == k:
                    break
                else:
                    print(' -> ' + chunks[n].surface(), end='')
            #j -> k -> 根
            print(' | ' + chunks[j_list[0]].noun_replace('Y'), end='')
            for n in j_list[1:]:
                if n == k:
                    print(' | ' + chunks[k].surface(), end='')
                else:
                    print(' -> ' + chunks[n].surface(), end='')
            print('')

if __name__ == '__main__':
    for chunks in allsentence:
        extract_path(chunks)
