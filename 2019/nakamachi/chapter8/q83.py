"""
83. 単語／文脈の頻度の計測
82の出力を利用し，以下の出現分布，および定数を求めよ．

f(t,c): 単語tと文脈語cの共起回数
f(t,∗): 単語tの出現回数
f(∗,c): 文脈語cの出現回数
N: 単語と文脈語のペアの総出現回数
"""
from collections import Counter

from utils import load_word_context_tab, save_counter, load_counter

# TODO: 不要なものを分ける
class Count:
    def __init__(self):
        word_context_tab_set_list = load_word_context_tab().split("\n")[:-1]
        word_context_tab_joined_list = list()
        main_word_list = list()
        context_word_list = list()

        for item in word_context_tab_set_list:
            item = item.split("\t")
            word_context_tab_joined_list.append("\t".join(item))
            main_word_list.append(item[0])
            context_word_list.append(item[1])

        self.word_context_counter = Counter(word_context_tab_joined_list)
        self.word_counter = Counter(main_word_list)
        self.context_word_counter = Counter(context_word_list)

        self.word_context_set_list = word_context_tab_joined_list
        self.main_word_list = main_word_list
        self.context_word_list = context_word_list


    def f_t_c(self, t, c):
        return self.word_context_counter[t + "\t" + c]

    def f_t(self, t):
        return self.word_counter[t]

    def f_c(self, c):
        return self.context_word_counter[c]

    def n(self):
        return len(self.word_context_set_list)

    def all_word_list(self):
        return list(set(self.main_word_list + self.context_word_list))

    def all_main_word_list(self):
        return list(set(self.main_word_list))

    def all_context_word_list(self):
        return list(set(self.context_word_list))


def main():
    c = Count()
    save_counter(c)
    c = load_counter()
    print(c.n())
    print(len(c.word_context_counter))
    # print(c.all_word_list())
    """
    output result
73077872
21598257
    """


if __name__ == '__main__':
    main()
